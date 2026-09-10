# Submission verification

## Actual Databricks execution

The packaged notebooks `01_run_pipeline.ipynb` and `02_evaluate_run.ipynb`
completed on Databricks Serverless using Spark 4.2.0. The run started at
2026-09-09 21:53 UTC (10 September in India). Its new table prefix was:

`workspace.default.pmfby_pipeline_r20260909_215304_179742_`

The check extracted the repository inputs, helper and notebooks into a fresh
directory and executed every code cell in order. Input files were checked against
the included checksums and read with explicit schemas. Original experiment tables
were not used as executable inputs and were not overwritten.

The downloadable receipt is `results/submission_runtime_validation.json`.
It records the actual Spark version, input hashes, published row counts,
acceptance checks and evaluation results.

- 4,497 master contexts retained in both Gold and scenario allocation.
- 2,000,000 unique scenarios: 505,731 simulated losses and 1,494,269 non-losses.
- Three fitted models, each with 366,591 test predictions.
- All 10 acceptance checks passed, including complete model inputs, disjoint
  time splits, one label per scenario, equal review capacity and exclusion of
  hidden truth from predictions and decisions.
- Evaluation recomputed all 18 policy/capacity totals from the new saved outputs.
- The RF-minus-rule recall difference at 20% capacity reproduced
  0.18813314037626627 percentage points. The fixed-queue context bootstrap
  interval also reproduced the historical result. This remains a conditional
  synthetic diagnostic, not evidence of a decisive real-world ML advantage.

MLflow model-artifact logging was disabled. Fitting, scoring and evaluation were
executed. The check does not certify optional MLflow permissions or integrations.

## Packaged code and local checks

After upload, notebook formatting was improved without changing Python syntax
trees. `results/code_verification.json` checks the executed notebook hashes against
the Databricks receipt and verifies each final code cell has the same Python AST
as the executed cell. Notebook 03 additionally needed a missing `import re` in
its bootstrap; the repaired bootstrap and daily-weather publication ran successfully, recorded in
`results/source_rebuild_validation.json`. The optional full rebuild was then stopped to preserve quota, so notebook 03 is NOT fully runtime-certified. Its feature formulas were unchanged.
Markdown and formatting changes do not change computation.

Eight local standard-library tests passed on 10 September 2026: notebook syntax,
all seven snapshot checksums/headers/row counts, master coverage and model inputs,
historical result arithmetic, independence from private source tables, identifier
validation, ten-slide presentation structure and individual upload file sizes.

## Limits of this verification

This verifies execution from the included prepared extracts. It does not rerun
external NASA/MODIS API acquisition or raw DES workbook preparation. Exact future
ML results can vary with Spark/runtime versions or execution details; preserved
historical results and this submission rerun remain separately identified.

The Word report was copied unchanged as requested. It is not certified as revised
by this packaging check. Export the final reviewed Word document to PDF to satisfy
the assignment's report-format requirement. The ZIP is a clean repository snapshot,
not evidence of trimester-long Git commit history.
