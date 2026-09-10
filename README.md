# PMFBY Claim Triage Intelligence

**MBA Big Data Analytics, NMIMS — Group C-II**

Which cases should enter the first human-verification batch when review capacity
is fixed? This project integrates agricultural context, NASA POWER weather and
MODIS vegetation, generates explicitly synthetic loss/non-loss scenarios, and
compares review queues using PySpark on Databricks.

The model does not approve insurance, reject claims or establish fraud. The
intended workflow retains human review for every case. Real settlement times,
assessor effort, cost savings and ROI were not measured.

## What is included

| Folder | Purpose |
|---|---|
| `notebooks/` | Three documented Databricks-compatible Jupyter notebooks |
| `src/` | Configuration, checksum validation and safe Delta publishing |
| `data/` | Seven compressed input/reference snapshots and their schemas/checksums |
| `results/` | Historical accepted results, evidence-tier comparison and sample worklist |
| `docs/` | Data lineage, assumptions, validation and rubric mapping |
| `reports/` | The user-supplied Word report, unchanged |
| `presentations/` | Revised 10-slide PowerPoint with speaker notes |
| 

The full two-million-row scenario table is generated in Databricks rather than
committed to GitHub. All inputs needed by the notebooks are included. **There is
no dependency on the original author's private Delta tables.** Source table names
inside `data/manifest.json` record provenance only.


## Prepared inputs and execution

The existing `.csv.gz` files are the input and reference snapshots
documented in `manifest.json`. Keep their filenames and locations unchanged.

Notebooks 01 and 02 reproduce the main experiment and evaluation from
the prepared snapshots; both completed runtime verification.

Notebook 03 demonstrates upstream weather matching and seasonal feature
preparation. Its runtime verification is incomplete. It does not process
the district-boundary ZIP or original DES files.

## Quick start: Databricks

1. Clone this complete repository into a **Databricks Git folder**. Alternatively,
   upload/extract the complete folder into a writable workspace directory. Keep
   `data/`, `src/`, `notebooks/` and `project_config.json` together.
2. Use Python compute with Spark/MLlib and Unity Catalog support. The current
   Databricks environment supplies PySpark; do not install a conflicting PySpark
   version. NumPy is required for the evaluation notebook.
3. In `project_config.json`, set `catalog` and `schema` to an existing schema where
   you can **CREATE TABLE, CREATE VOLUME, and read/write the created volumes**.
   The supplied defaults are `workspace` and `default`. No password or token
   belongs in this file. The repository/workspace folder must also be writable
   for the ignored `artifacts/` run pointer.
4. Open **`notebooks/01_run_pipeline.ipynb`** and run its cells in order. Default:
   **2,000,000 scenarios**, seed **20260907**, simulation version **2.2.0**.
   The notebook locates the repository automatically; set its `PROJECT_ROOT`
   variable only if your workspace layout prevents discovery.
5. Continue with **`notebooks/02_evaluate_run.ipynb`**. It reads the completed run
   pointer, verifies saved totals and produces evidence-tier/worklist/bootstrap
   diagnostics without fitting models again.
6. Optional: run **`notebooks/03_rebuild_source_features.ipynb`** to demonstrate
   the upstream spatial matching, seasonal weather features and MODIS anomalies.
   It writes separate preparation tables. It does not silently replace the
   historical snapshots used by notebook 01.

Every execution creates a new timestamped table prefix. Existing runs are never
overwritten. Tables remain after a failed run for inspection. Only a run with
all acceptance checks and a completion record is complete.

MLflow model logging is optional (`log_models_to_mlflow`, default `false`). It
requires the workspace's normal experiment/model-artifact permissions. Disabling
logging does not disable model fitting, predictions, metrics or policy evaluation.

## Architecture and scope

Prepared PMFBY/DES/geography master + NASA daily extract + MODIS seasonal extract
→ spatial/calendar/feature engineering → context snapshots → full-context repair
and explicit missingness → synthetic scenarios / hidden truth / labels in separate
tables → LR and RF → predictions → equal-capacity queues → evaluation.

Notebook 03 begins at **provided source extracts**, not at scraping external APIs
or parsing the original DES workbook. Notebook 01 deliberately replays the final
experiment from its exact intermediate snapshots. This boundary is explicit so
the source-engineering demonstration and the final result can both be inspected
without silently changing the experiment.

## Accepted historical results

These numbers describe the original accepted **7 September 2026 run**, not an
automatic claim about every new execution. Exact values are in
`results/historical_run.json` and `results/historical_evaluation.json`.

- **4,497** district-season-year contexts; **2,000,000** synthetic scenarios.
- **505,731 simulated losses** and **1,494,269 non-losses**.
- Training: 20% deterministic sample of 2018–2020; validation: 2021; test: 2022.
- LR ROC AUC **0.5653**; full RF **0.5719**; base-feature RF **0.5670**.
- At 20% review capacity, loss recall: random **19.94%**, rule **27.78%**, RF
  **27.97%**. RF adds **182 simulated losses**, approximately **0.19 percentage
  points of recall**, over the rule at the same capacity.
- Conditional paired-context bootstrap interval for RF minus rule:
  **−1.51 to +2.00 percentage points**. It does not establish a conclusive advantage.
- The expected-probability diagnostic reaches AUC **0.594**. It explains the
  simulation's limited discrimination; it is not a universal ceiling or a measure
  of real-world claim accuracy.
- Selected classification thresholds labelled all test cases positive. Ranking
  remains evaluable; useful binary classification was not established.

All three models assign identical scores within a context. The test has 843
contexts. Two million scenarios demonstrate a processing workload, not two
million independent real observations.



## Limitations and recommended next step

The simulator thresholds are assumptions, not empirically calibrated loss rules.
Regional estimates remain distinguishable from observed evidence. Seasonal data
does not prove individual field loss, and publication-time availability was not
reconstructed. One seed and one test year limit robustness claims.

Retain the transparent rule as a supervised comparison baseline. Verified CCE,
yield-shortfall or technology-based yield estimates would enable real validation.
Historical approval/rejection outcomes can reflect administration and selection
bias, so they are not the preferred loss target. Better real-world performance is
an open empirical question, not a promised consequence of obtaining more data.
