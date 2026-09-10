# Exported data dictionary

Schemas below come from the exported Spark tables. Exact field order/types also appear in `data/manifest.json`.

## Layer conventions

- `*_model`: observed value or a model-only estimate; never relabel an estimate as an observation.
- `*_missing`: 1 means unavailable before model filling; 0 means available.
- `*_fill_method`: how the model input was obtained.
- `evidence_tier`: completeness/fallback category, not farmer fairness or risk.
- `context_key`: district-season-year context identifier.
- Gold is context data; scenario labels and hidden simulator truth are generated separately.

## source_master

Rows: 4,497

| Field | Spark type | Nullable in source schema |
|---|---|---|
| `district_censuscode` | double | true |
| `state` | string | true |
| `district` | string | true |
| `year` | long | true |
| `season` | string | true |
| `centroid_lat` | double | true |
| `centroid_lon` | double | true |
| `coverage_n_crops` | long | true |
| `coverage_n_policy_rows` | long | true |
| `coverage_sum_insured_total` | double | true |
| `coverage_avg_premium_rate` | double | true |
| `coverage_sum_farmerShareValue` | double | true |
| `coverage_sum_goiShareValue` | double | true |
| `coverage_sum_stateShareValue` | double | true |
| `coverage_n_insurance_companies` | long | true |
| `stats_farmerCount` | double | true |
| `stats_loaneeCount` | double | true |
| `stats_nonLoaneeCount` | double | true |
| `stats_areaInsured_th_ha` | double | true |
| `stats_sumInsured_lac` | double | true |
| `stats_farmerShare_lac` | double | true |
| `stats_goiShare_lac` | double | true |
| `stats_stateShare_lac` | double | true |
| `stats_iuCount` | double | true |
| `stats_grossPremium_lac` | double | true |
| `stats_district.gender.male (%)` | double | true |
| `stats_district.gender.female (%)` | double | true |
| `stats_district.gender.transgender (%)` | double | true |
| `stats_district.category.sc (%)` | double | true |
| `stats_district.category.st (%)` | double | true |
| `stats_district.category.obc (%)` | double | true |
| `stats_district.category.gen (%)` | double | true |
| `stats_district.type.marginal (%)` | double | true |
| `stats_district.type.small (%)` | double | true |
| `stats_district.type.other (%)` | double | true |
| `des_total_area_hectare` | double | true |
| `des_total_production_tonnes` | double | true |
| `des_n_crops_reported` | double | true |
| `des_n_crops_excluded_from_tonnes_sum` | double | true |
| `des_value_is_annual_not_season_specific` | boolean | true |
| `state_2011_raw` | string | true |
| `district_2011_raw` | string | true |
| `weather_temp_mean_c` | string | true |
| `weather_precip_total_mm` | string | true |
| `weather_precip_anomaly_pct` | string | true |
| `weather_humidity_mean_pct` | string | true |
| `ndvi_mean` | string | true |
| `ndvi_anomaly` | string | true |
| `evi_mean` | string | true |
| `district_resolved` | boolean | true |
| `source_statistics_available` | boolean | true |
| `source_des_available` | boolean | true |
| `source_weather_available` | boolean | true |
| `source_vegetation_available` | boolean | true |
| `coverage_insured_per_policy_row` | double | true |
| `coverage_farmer_premium_share_pct` | double | true |
| `coverage_government_subsidy_share_pct` | double | true |
| `stats_loanee_share` | double | true |
| `stats_small_marginal_share` | double | true |
| `coverage_insured_prior_zscore` | double | true |
| `coverage_policy_rows_prior_zscore` | double | true |
| `des_area_prior_zscore` | double | true |
| `eligible_for_synthetic_base` | boolean | true |
| `weather_ready` | boolean | true |
| `model_ready_after_external_features` | boolean | true |
| `feature_schema_version` | string | true |

## nasa_daily

Rows: 838,726

| Field | Spark type | Nullable in source schema |
|---|---|---|
| `grid_lat` | double | true |
| `grid_lon` | double | true |
| `observation_date` | date | true |
| `temp_mean_c` | double | true |
| `precip_mm` | double | true |
| `humidity_mean_pct` | double | true |
| `source` | string | true |

## modis_seasonal

Rows: 5,730

| Field | Spark type | Nullable in source schema |
|---|---|---|
| `system:index` | string | true |
| `district` | string | true |
| `evi_mean` | double | true |
| `ndvi_mean` | double | true |
| `season` | string | true |
| `source` | string | true |
| `spatial_resolution_m` | long | true |
| `state` | string | true |
| `year` | long | true |
| `.geo` | string | true |

## base_gold

Rows: 4,497

| Field | Spark type | Nullable in source schema |
|---|---|---|
| `state_key` | string | true |
| `district_key` | string | true |
| `year` | integer | true |
| `season` | string | true |
| `grid_lat` | double | true |
| `grid_lon` | double | true |
| `centroid_lat` | double | true |
| `centroid_lon` | double | true |
| `district_censuscode` | long | true |
| `state` | string | true |
| `district` | string | true |
| `coverage_n_crops` | long | true |
| `coverage_n_source_rows` | long | true |
| `coverage_sum_insured_total` | double | true |
| `coverage_avg_premium_rate` | double | true |
| `coverage_sum_farmerShareValue` | double | true |
| `coverage_sum_goiShareValue` | double | true |
| `coverage_sum_stateShareValue` | double | true |
| `coverage_n_insurance_companies` | long | true |
| `stats_farmerCount` | double | true |
| `stats_loaneeCount` | double | true |
| `stats_nonLoaneeCount` | double | true |
| `stats_areaInsured_th_ha` | double | true |
| `stats_sumInsured_lac` | double | true |
| `stats_farmerShare_lac` | double | true |
| `stats_goiShare_lac` | double | true |
| `stats_stateShare_lac` | double | true |
| `stats_iuCount` | double | true |
| `stats_grossPremium_lac` | double | true |
| `stats_district_gender_male` | double | true |
| `stats_district_gender_female` | double | true |
| `stats_district_gender_transgender` | double | true |
| `stats_district_category_sc` | double | true |
| `stats_district_category_st` | double | true |
| `stats_district_category_obc` | double | true |
| `stats_district_category_gen` | double | true |
| `stats_district_type_marginal` | double | true |
| `stats_district_type_small` | double | true |
| `stats_district_type_other` | double | true |
| `des_total_area_hectare` | double | true |
| `des_total_production_tonnes` | double | true |
| `des_n_crops_reported` | double | true |
| `des_n_crops_excluded_from_tonnes_sum` | double | true |
| `des_value_is_annual_not_season_specific` | boolean | true |
| `state_2011_raw` | string | true |
| `district_2011_raw` | string | true |
| `district_resolved` | boolean | true |
| `source_statistics_available` | boolean | true |
| `source_des_available` | boolean | true |
| `coverage_farmer_premium_share_pct` | double | true |
| `coverage_government_subsidy_share_pct` | double | true |
| `stats_loanee_share` | double | true |
| `stats_small_marginal_share` | double | true |
| `des_area_prior_zscore` | double | true |
| `eligible_for_synthetic_base` | boolean | true |
| `context_key` | string | true |
| `weather_grid_distance_km` | double | true |
| `weather_grid_accepted` | boolean | true |
| `weather_grid_method` | string | true |
| `season_end` | date | true |
| `weather_expected_days` | integer | true |
| `weather_temp_valid_days` | long | true |
| `weather_precip_valid_days` | long | true |
| `weather_humidity_valid_days` | long | true |
| `weather_temp_mean_c` | double | true |
| `weather_precip_total_mm` | double | true |
| `weather_humidity_mean_pct` | double | true |
| `weather_temp_max_daily_mean_c` | double | true |
| `weather_dry_days_lt_1mm` | long | true |
| `weather_heat_days_mean_ge_35c` | long | true |
| `weather_heavy_rain_days_ge_20mm` | long | true |
| `weather_heavy_rain_days_ge_50mm` | long | true |
| `weather_max_daily_precip_mm` | double | true |
| `weather_max_3day_precip_mm` | double | true |
| `weather_precip_sd_mm` | double | true |
| `weather_max_consecutive_dry_days` | long | true |
| `weather_valid_day_share` | double | true |
| `weather_ready` | boolean | true |
| `weather_history_years` | long | true |
| `weather_prior_precip_mm` | double | true |
| `weather_precip_anomaly_pct` | double | true |
| `ndvi_mean` | double | true |
| `evi_mean` | double | true |
| `ndvi_history_years` | long | true |
| `ndvi_prior_mean` | double | true |
| `ndvi_anomaly` | double | true |
| `vegetation_source` | string | true |
| `coverage_insured_prior_zscore` | double | true |
| `source_vegetation_available` | boolean | true |
| `source_weather_available` | boolean | true |
| `satellite_join_status` | string | true |
| `model_ready_after_external_features` | boolean | true |
| `feature_schema_version` | string | true |
| `prediction_time_scope` | string | true |

## weather_seasonal

Rows: 4,310

| Field | Spark type | Nullable in source schema |
|---|---|---|
| `grid_lat` | double | true |
| `grid_lon` | double | true |
| `year` | long | true |
| `season` | string | true |
| `season_end` | date | true |
| `weather_expected_days` | integer | true |
| `weather_temp_valid_days` | long | true |
| `weather_precip_valid_days` | long | true |
| `weather_humidity_valid_days` | long | true |
| `weather_temp_mean_c` | double | true |
| `weather_precip_total_mm` | double | true |
| `weather_humidity_mean_pct` | double | true |
| `weather_temp_max_daily_mean_c` | double | true |
| `weather_dry_days_lt_1mm` | long | true |
| `weather_heat_days_mean_ge_35c` | long | true |
| `weather_heavy_rain_days_ge_20mm` | long | true |
| `weather_heavy_rain_days_ge_50mm` | long | true |
| `weather_max_daily_precip_mm` | double | true |
| `weather_max_3day_precip_mm` | double | true |
| `weather_precip_sd_mm` | double | true |
| `weather_max_consecutive_dry_days` | long | true |
| `weather_valid_day_share` | double | true |
| `weather_ready` | boolean | true |
| `weather_history_years` | long | true |
| `weather_prior_precip_mm` | double | true |
| `weather_precip_anomaly_pct` | double | true |

## vegetation_seasonal

Rows: 5,730

| Field | Spark type | Nullable in source schema |
|---|---|---|
| `state_key` | string | true |
| `district_key` | string | true |
| `year` | integer | true |
| `season` | string | true |
| `ndvi_mean` | double | true |
| `evi_mean` | double | true |
| `ndvi_history_years` | long | true |
| `ndvi_prior_mean` | double | true |
| `ndvi_anomaly` | double | true |
| `vegetation_source` | string | true |

## final_master

Rows: 4,497

| Field | Spark type | Nullable in source schema |
|---|---|---|
| `year` | integer | true |
| `season` | string | true |
| `state_key` | string | true |
| `grid_lat` | double | true |
| `grid_lon` | double | true |
| `centroid_lat` | double | true |
| `centroid_lon` | double | true |
| `district_key` | string | true |
| `district_censuscode` | long | true |
| `state` | string | true |
| `district` | string | true |
| `coverage_n_crops` | long | true |
| `coverage_n_source_rows` | long | true |
| `coverage_sum_insured_total` | double | true |
| `coverage_avg_premium_rate` | double | true |
| `coverage_sum_farmerShareValue` | double | true |
| `coverage_sum_goiShareValue` | double | true |
| `coverage_sum_stateShareValue` | double | true |
| `coverage_n_insurance_companies` | long | true |
| `stats_farmerCount` | double | true |
| `stats_loaneeCount` | double | true |
| `stats_nonLoaneeCount` | double | true |
| `stats_areaInsured_th_ha` | double | true |
| `stats_sumInsured_lac` | double | true |
| `stats_farmerShare_lac` | double | true |
| `stats_goiShare_lac` | double | true |
| `stats_stateShare_lac` | double | true |
| `stats_iuCount` | double | true |
| `stats_grossPremium_lac` | double | true |
| `stats_district_gender_male` | double | true |
| `stats_district_gender_female` | double | true |
| `stats_district_gender_transgender` | double | true |
| `stats_district_category_sc` | double | true |
| `stats_district_category_st` | double | true |
| `stats_district_category_obc` | double | true |
| `stats_district_category_gen` | double | true |
| `stats_district_type_marginal` | double | true |
| `stats_district_type_small` | double | true |
| `stats_district_type_other` | double | true |
| `des_total_area_hectare` | double | true |
| `des_total_production_tonnes` | double | true |
| `des_n_crops_reported` | double | true |
| `des_n_crops_excluded_from_tonnes_sum` | double | true |
| `des_value_is_annual_not_season_specific` | boolean | true |
| `state_2011_raw` | string | true |
| `district_2011_raw` | string | true |
| `district_resolved` | boolean | true |
| `source_statistics_available` | boolean | true |
| `source_des_available` | boolean | true |
| `coverage_farmer_premium_share_pct` | double | true |
| `coverage_government_subsidy_share_pct` | double | true |
| `stats_loanee_share` | double | true |
| `stats_small_marginal_share` | double | true |
| `des_area_prior_zscore` | double | true |
| `eligible_for_synthetic_base` | boolean | true |
| `context_key` | string | true |
| `weather_grid_distance_km` | double | true |
| `weather_grid_accepted` | boolean | true |
| `weather_grid_method` | string | true |
| `ndvi_mean` | double | true |
| `evi_mean` | double | true |
| `ndvi_history_years` | long | true |
| `ndvi_prior_mean` | double | true |
| `ndvi_anomaly` | double | true |
| `vegetation_source` | string | true |
| `coverage_insured_prior_zscore` | double | true |
| `source_vegetation_available` | boolean | true |
| `source_weather_available` | boolean | true |
| `satellite_join_status` | string | true |
| `model_ready_after_external_features` | boolean | true |
| `feature_schema_version` | string | true |
| `prediction_time_scope` | string | true |
| `centroid_recovered` | boolean | true |
| `season_end` | date | true |
| `weather_expected_days` | integer | true |
| `weather_temp_valid_days` | long | true |
| `weather_precip_valid_days` | long | true |
| `weather_humidity_valid_days` | long | true |
| `weather_temp_mean_c` | double | true |
| `weather_precip_total_mm` | double | true |
| `weather_humidity_mean_pct` | double | true |
| `weather_temp_max_daily_mean_c` | double | true |
| `weather_dry_days_lt_1mm` | long | true |
| `weather_heat_days_mean_ge_35c` | long | true |
| `weather_heavy_rain_days_ge_20mm` | long | true |
| `weather_heavy_rain_days_ge_50mm` | long | true |
| `weather_max_daily_precip_mm` | double | true |
| `weather_max_3day_precip_mm` | double | true |
| `weather_precip_sd_mm` | double | true |
| `weather_max_consecutive_dry_days` | long | true |
| `weather_valid_day_share` | double | true |
| `weather_ready` | boolean | true |
| `weather_history_years` | long | true |
| `weather_prior_precip_mm` | double | true |
| `weather_precip_anomaly_pct` | double | true |
| `vegetation_recovered` | boolean | true |
| `coverage_avg_premium_rate_model` | double | true |
| `coverage_avg_premium_rate_fill_method` | string | true |
| `coverage_avg_premium_rate_missing` | double | true |
| `coverage_n_crops_model` | double | true |
| `coverage_n_crops_fill_method` | string | true |
| `coverage_n_crops_missing` | double | true |
| `weather_temp_mean_c_model` | double | true |
| `weather_temp_mean_c_fill_method` | string | true |
| `weather_temp_mean_c_missing` | double | true |
| `ndvi_mean_model` | double | true |
| `ndvi_mean_fill_method` | string | true |
| `ndvi_mean_missing` | double | true |
| `evi_mean_model` | double | true |
| `evi_mean_fill_method` | string | true |
| `evi_mean_missing` | double | true |
| `weather_temp_max_daily_mean_c_model` | double | true |
| `weather_temp_max_daily_mean_c_fill_method` | string | true |
| `weather_temp_max_daily_mean_c_missing` | double | true |
| `weather_dry_days_lt_1mm_model` | double | true |
| `weather_dry_days_lt_1mm_fill_method` | string | true |
| `weather_dry_days_lt_1mm_missing` | double | true |
| `weather_heat_days_mean_ge_35c_model` | double | true |
| `weather_heat_days_mean_ge_35c_fill_method` | string | true |
| `weather_heat_days_mean_ge_35c_missing` | double | true |
| `weather_heavy_rain_days_ge_20mm_model` | double | true |
| `weather_heavy_rain_days_ge_20mm_fill_method` | string | true |
| `weather_heavy_rain_days_ge_20mm_missing` | double | true |
| `weather_heavy_rain_days_ge_50mm_model` | double | true |
| `weather_heavy_rain_days_ge_50mm_fill_method` | string | true |
| `weather_heavy_rain_days_ge_50mm_missing` | double | true |
| `weather_max_consecutive_dry_days_model` | double | true |
| `weather_max_consecutive_dry_days_fill_method` | string | true |
| `weather_max_consecutive_dry_days_missing` | double | true |
| `weather_max_daily_precip_mm_model` | double | true |
| `weather_max_daily_precip_mm_fill_method` | string | true |
| `weather_max_daily_precip_mm_missing` | double | true |
| `weather_max_3day_precip_mm_model` | double | true |
| `weather_max_3day_precip_mm_fill_method` | string | true |
| `weather_max_3day_precip_mm_missing` | double | true |
| `ndvi_anomaly_model` | double | true |
| `ndvi_anomaly_missing` | double | true |
| `ndvi_anomaly_fill_method` | string | true |
| `weather_precip_anomaly_pct_model` | double | true |
| `weather_precip_anomaly_pct_missing` | double | true |
| `weather_precip_anomaly_pct_fill_method` | string | true |
| `weather_valid_day_share_model` | double | true |
| `weather_valid_day_share_missing` | double | true |
| `weather_valid_day_share_fill_method` | string | true |
| `feature_imputation_count` | double | true |
| `evidence_tier` | string | true |
| `previous_model_ready` | boolean | true |
