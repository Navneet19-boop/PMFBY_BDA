# Architecture and lineage

## Input boundary

The bundle exports seven Delta snapshots at version 0. `data/manifest.json`
records original table names, schemas, row counts and SHA-256 for each compressed
file. Runtime code reads those files, not the original table names.

| Snapshot | Rows | Role |
|---|---:|---|
| source_master | 4,497 | Prepared PMFBY/DES/geography input; not a raw farmer database |
| nasa_daily | 838,726 | Daily weather extraction used by the original engineering stage |
| modis_seasonal | 5,730 | Existing seasonal satellite extraction |
| base_gold | 4,497 | Historical intermediate Gold before full-context repair |
| weather_seasonal | 4,310 | Historical engineered seasonal weather, indexed by request location |
| vegetation_seasonal | 5,730 | Historical engineered vegetation and prior-year anomalies |
| final_master | 4,497 | Reference final Gold for inspection; never training outcome truth |

Exports use compressed CSV with round-trip numeric precision and the original
Spark schemas. Files are checked before staging in a Unity Catalog Volume.
CSV does not preserve the distinction between an empty string and a null string;
the model-relevant numeric fields, counts and generated labels must be checked
when validating a replay. Original Delta execution evidence remains separate.

## Engineering

Notebook 03 normalises source names/types, checks key uniqueness, masks invalid
weather/vegetation values, matches district centroids to the nearest available
NASA request location and constructs complete seasonal calendars. It calculates
dry spells, heat/rain counts and historical anomalies using earlier years only.

Notebook 01 starts from the exact intermediate snapshots. It recovers documented
centroids and MODIS name matches, retains every context, and creates model-only
estimates with explicit fill-method and missingness fields. Some legacy flags
describe the earlier join; use the recovery fields, fill methods and missingness
indicators to understand final evidence provenance.

## Table separation

| Output | Meaning and allowed use |
|---|---|
| gold, fill_audit, coverage | Observations/derived evidence, estimates and provenance |
| allocation | Synthetic scenario count per context, not a farmer population count |
| synthetic_claims | Observable model inputs and synthetic identifiers/amount proxy |
| hidden_truth | Simulator probability and sampled event; excluded from operational scoring |
| labels | Synthetic binary target; training and held-out evaluation only |
| model_predictions | Model scores without truth or labels |
| policy_rankings, policy_decisions | Observable/predicted ranking and fixed-capacity decisions |
| capacity_comparison | Labels joined only after decisions are persisted |
| triage_routes | Human-review workflow; no binding insurance entitlement decision |
| acceptance_checks, run_manifest | Execution evidence and checks |

The policy comparison uses six strategies and identical 10%, 20%, 30% case-count
budgets. A deterministic ID breaks ties. The bootstrap in notebook 02 resamples
paired context contributions to existing queues: it neither retrains nor reranks,
and each resample need not retain exactly the original capacity share.

## Reproduction boundaries

The primary notebook and evaluation are the final run path. The upstream rebuild
is optional and cannot change the primary notebook's input snapshots silently.
Changing the seed, scenario count, simulation version, data or runtime defines a
new experiment. Spark aggregation/model numerics can vary between runtimes.
Historical results are not overwritten by fresh execution results.

This repository does not reconstruct external API requests, MODIS extraction
credentials, the original DES workbook parsing or field-level ground truth.
The included source extracts make execution independent of those services.
