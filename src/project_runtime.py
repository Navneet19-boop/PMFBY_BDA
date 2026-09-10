"""Input snapshots, safe Delta publishing and run configuration.

This module never reads credentials or connects to a private source table.
Databricks supplies the authenticated Spark session. Input table names in the
data manifest are provenance records only; execution reads the bundled files.
"""

import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter


def locate_project(start=None):
    """Find the repository from a notebook's working directory."""
    current = Path(start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "project_config.json").is_file():
            return candidate
    raise FileNotFoundError(
        "Open the notebook inside the complete repository, or set PROJECT_ROOT "
        "to its absolute workspace path. Importing only the notebook is insufficient."
    )


def file_sha256(path):
    """Hash a file without loading the whole file into memory."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def checked_identifier(value):
    """Restrict configuration to simple, unquoted SQL identifiers."""
    if not re.fullmatch(r"[a-z][a-z0-9_]*", value):
        raise ValueError(f"Use lowercase letters, digits and underscores: {value!r}")
    return value


class ProjectRuntime:
    """One isolated execution namespace with immutable input checksums."""

    def __init__(self, spark, root=None, run_kind="pipeline"):
        self.spark = spark
        self.root = locate_project(root)
        self.config = json.loads((self.root / "project_config.json").read_text())
        self.manifest = json.loads((self.root / "data/manifest.json").read_text())
        catalog = checked_identifier(self.config["catalog"])
        schema = checked_identifier(self.config["schema"])
        self.namespace = f"{catalog}.{schema}"
        self.run_id = datetime.now(timezone.utc).strftime("r%Y%m%d_%H%M%S_%f")
        kind = checked_identifier(run_kind)
        self.prefix = f"{self.namespace}.pmfby_{kind}_{self.run_id}_"
        self.source_versions = {}
        self.published = {}
        self.timings = []
        self.started = perf_counter()
        self.input_volume = f"{self.namespace}.pmfby_submission_inputs"
        self.input_directory = Path(
            f"/Volumes/{catalog}/{schema}/pmfby_submission_inputs"
        )
        # The user needs CREATE VOLUME and CREATE TABLE in this schema.
        spark.sql(f"CREATE VOLUME IF NOT EXISTS {self.input_volume}")

    def read_snapshot(self, name):
        """Verify bundled CSV bytes, stage them in a Volume, and read with Spark.

        Spark uses the exported schema rather than inferring numeric identifiers.
        Large daily weather data is parsed by Spark, not collected on the driver.
        """
        from pyspark.sql.types import StructType

        entry = self.manifest["tables"][name]
        source = (self.root / "data" / entry["file"]).resolve()
        if source.parent != (self.root / "data").resolve():
            raise ValueError("Snapshot files must be directly inside data/")
        if file_sha256(source) != entry["sha256"]:
            raise ValueError(f"Input checksum mismatch: {name}")
        destination = self.input_directory / entry["sha256"] / source.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            if file_sha256(destination) != entry["sha256"]:
                raise ValueError(f"Existing staged input changed: {destination}")
        else:
            shutil.copyfile(source, destination)
        frame = (
            self.spark.read.schema(StructType.fromJson(entry["schema"]))
            .option("header", "true")
            .option("mode", "FAILFAST")
            .option("multiLine", "true")
            .option("escape", '"')
            .csv(str(destination))
        )
        actual = frame.count()
        if actual != entry["rows"]:
            raise ValueError(f"{name}: expected {entry['rows']} rows, found {actual}")
        self.source_versions[name] = {
            "file": entry["file"],
            "sha256": entry["sha256"],
            "original_delta_version": entry["delta_version"],
            "rows": actual,
        }
        return frame

    def table(self, name):
        return self.prefix + checked_identifier(name)

    def publish(self, frame, name, partition_cols=None):
        """CREATE a new Delta table; never replace an earlier run."""
        target = self.table(name)
        started = perf_counter()
        view = f"stage_{self.run_id}_{checked_identifier(name)}"
        frame.createOrReplaceTempView(view)
        partition = ""
        if partition_cols:
            columns = ", ".join(checked_identifier(c) for c in partition_cols)
            partition = f" PARTITIONED BY ({columns})"
        self.spark.sql(
            f"CREATE TABLE {target} USING DELTA{partition} AS SELECT * FROM {view}"
        )
        result = self.spark.table(target)
        count = result.count()
        self.published[name] = count
        self.timings.append((name, float(perf_counter() - started), count))
        print(f"PUBLISHED {name}: {count:,} rows", flush=True)
        return result

    def record_completion(self, extra=None):
        """Save the run pointer used by the separate evaluation notebook."""
        output = self.root / "artifacts"
        output.mkdir(exist_ok=True)
        record = {
            "status": "complete",
            "run_id": self.run_id,
            "prefix": self.prefix,
            "source_versions": self.source_versions,
            "published_rows": self.published,
            "spark_version": self.spark.version,
            **(extra or {}),
        }
        (output / "latest_run.json").write_text(json.dumps(record, indent=2))
        return record
