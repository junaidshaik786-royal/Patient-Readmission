# KPI Dictionary and Data-Grain Rules

| KPI | Definition | Recomputed value |
|---|---|---:|
| Encounter count | Count of encounter records | 101,766 |
| Distinct patients | Count of distinct patient_nbr values | 71,518 |
| Early readmissions | Count of readmitted = <30 | 11,357 |
| Early readmission proportion | <30 count divided by all encounter records | 11.16% |
| Later readmissions | Count of readmitted = >30 | 35,545 |
| No recorded readmission | Count of readmitted = NO | 54,864 |
| Mean length of stay | Average time_in_hospital | 4.40 days |
| Mean medications | Average num_medications | 16.02 |
| Mean lab procedures | Average num_lab_procedures | 43.10 |
| Age-band early readmission proportion | Age-band <30 encounters / all age-band encounters | See outputs/age_group_readmission_rates.csv |

## Reporting rules
1. Clearly distinguish encounter counts from unique patient counts.
2. Describe the 11.16% figure as an encounter-level descriptive percentage, **not patient-level risk**.
3. Maintain NO, >30, <30 as separate readmission categories.
4. Include subgroup counts beside rates to avoid misleading conclusions from small groups.
5. Treat '?' as missing in categorical fields; document whether such rows are excluded from denominators.
6. These results are unadjusted and refer to historical 1999–2008 source data, not current hospital performance.

## Missingness in supplied source CSV
| Field | Missing records | Percent |
|---|---:|---:|
| weight | 98,569 | 96.86% |
| medical_specialty | 49,949 | 49.08% |
| payer_code | 40,256 | 39.56% |
| race | 2,273 | 2.23% |
| diag_1 | 21 | 0.02% |

See [Data Source](DATA_SOURCE.md) for source and dataset fingerprint.
