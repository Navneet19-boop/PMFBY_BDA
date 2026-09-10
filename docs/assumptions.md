# Decisions and assumptions

These are the existing experimental choices. None of the loss-probability
increments is claimed to be calibrated to verified PMFBY loss outcomes.

| Choice | Mechanical effect | Why this value | Alternatives / evidence gap |
|---|---|---|---|
| Haversine radius 6,371.0088 km | Converts angular separation to km | Conventional mean-Earth approximation | Ellipsoidal alternatives not compared |
| Nearest request location, <=75 km | Limits accepted spatial separation | Engineering cutoff | 50/100 km not compared; not loss-calibrated |
| Kharif Jun–Oct; Rabi Nov–Apr | Defines complete season calendars, with leap days | Fixed project calendar | District/crop-specific calendars not compared |
| Temperature −90 to 65°C; rain 0–3,000 mm; humidity 0–100% | Masks out-of-range source values | Broad sanity checks | Not crop-damage thresholds or an outlier optimisation |
| NDVI/EVI in [−1,1] | Masks out-of-range vegetation values | Broad index sanity check in existing code | Per-observation QA/crop masks unavailable |
| >=95% valid temperature/rain days | Flags weather completeness | Engineering completeness rule | Alternative completeness cutoffs not compared |
| Dry <1 mm; heat daily mean >=35°C | Counts dry/heat days | Assumed feature definitions | Not calibrated against verified damage |
| Rain >=20 mm and >=50 mm | Two separate event counts | Assumed feature definitions | Other thresholds not tested |
| Maximum 3-day rainfall | Sums only windows with three observed days | Short event window | Other windows not compared |
| >=2 earlier years for anomalies | Avoids a baseline from only one earlier year | Minimum-history compromise | Longer baselines unavailable within the chosen period |
| State-year-season median, then year-season median | Fills model inputs while retaining raw fields/flags | Simple transparent recovery of incomplete contexts | Alternative imputation and uncertainty models not tested |
| Missing anomalies -> 0 plus missing flag | Supplies a neutral numeric placeholder | Enables all-context modelling without inventing history | Zero is not evidence of normal observed conditions |
| 2,000,000 scenarios | Creates a distributed synthetic workload | Academic experiment size | Not an estimate of the real farmer population |
| Minimum one per context; remainder 50% uniform / 50% exposure | Keeps all contexts and introduces exposure weighting | Explicit scenario-design compromise | Other allocations not sensitivity-tested |
| Seed 20260907 and named hash streams | Repeats IDs, sampling, amount and outcome draws | Reproducibility convention | Other seeds not tested in the reported experiment |
| Amount = exposure / count × (0.75 + 0.5U) | Introduces synthetic amount variation | Assumed bounded spread | Not an observed claim amount distribution |
| Base loss probability 0.07 | Starts every simulated risk at 7% | Uncalibrated assumption | No empirical PMFBY probability fit |
| Rain anomaly <=−30: +0.22; otherwise <=−10: +0.10 | Adds one rainfall contribution | Uncalibrated stress assumption | Thresholds/increments not sensitivity-tested |
| NDVI anomaly <=−0.15: +0.20; otherwise <=−0.05: +0.08 | Adds one vegetation contribution | Uncalibrated stress assumption | Continuous alternatives not compared |
| Maximum daily-mean temperature >=30: +0.08 | Adds temperature contribution | Uncalibrated assumption | Different from the 35°C heat-day feature definition |
| >=3 days with rain >=20 mm: +0.05 | Adds rainfall-event contribution independently | Uncalibrated assumption | Event severity/crop dependence not fitted |
| U(0,0.12) hidden shock; clip probability [0.02,0.95] | Adds latent variation and bounds probability | Deliberate simulation randomness | Shock ranges and alternative mechanisms not tested |
| Independent U(0,1) below probability -> loss | Samples binary outcomes, including non-losses | Bernoulli event mechanism | Synthetic events are not historical approvals/rejections |
| Train 2018–20, validate 2021, test 2022 | Separates fitting, threshold selection and final evaluation | Available temporal split | Multi-year or unseen-district robustness not established |
| 20% training sample | Reduces fitting workload | Compute constraint | Larger training samples not systematically compared |
| LR 60 iterations, regParam 0.01 | Fits regularised logistic regression | Fixed engineering/compute settings | No hyperparameter search |
| RF 60 trees, depth 8 | Bounds model size and complexity | Compute constraint | No hyperparameter search |
| StandardScaler, no mean centring | Scales numeric inputs using training data | Shared modelling pipeline | Alternative scaling not compared |
| Threshold grid 0.05–0.65, step 0.05 | Chooses validation positive-class F1 threshold | Small inexpensive search | Test thresholds were not retuned; final classification remained all-positive |
| Rule: one point for rain <=−10, NDVI <=−0.05, daily-mean max >=30 | Transparent observable comparator | Simple baseline | Not calibrated or proven optimal |
| Review capacity 10%, 20%, 30% | Equal case-count budgets for every strategy | Illustrative evaluated scenarios | Not an optimised staff-hours allocation |
| Fast-review score <=0.15 and completeness >=0.99 | Optional human-review route | Illustrative routing assumption | Not an entitlement decision; no cases entered this route in historical results |
| Bootstrap 2,000 replicates, seed 20260908 | Paired context resampling of fixed queues | Modest compute / repeatability | No retraining, reranking or district-level dependence correction |

The expected-probability diagnostic substitutes the hidden shock's mean 0.06.
It is excluded from operational competition. It does not establish a universal
AUC ceiling, real-world calibration or an entitlement decision threshold.
