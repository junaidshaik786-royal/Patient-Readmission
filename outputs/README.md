# Analysis outputs

This folder contains a small aggregated result used to show how the recorded `<30` readmission label varies by age band. It is a summary table, not patient-level data.

## File

- [`age_group_readmission_rates.csv`](age_group_readmission_rates.csv) — one row per age band, with the number of encounters, the number labelled `<30`, and the percentage within that age band.

## Columns

| Column | Meaning |
|---|---|
| `age_band` | The age range recorded in the source dataset. These are pre-grouped bands, not exact ages. |
| `encounters` | Number of encounter records in the age band. |
| `readmitted_lt30_encounters` | Number of encounters in the band labelled `<30`. |
| `readmitted_lt30_percent` | `<30` encounters divided by all encounters in that band, multiplied by 100 and rounded to two decimal places. |

For example, the 20–30 band contains 1,657 encounters, of which 236 (14.24%) are labelled `<30`. That is a descriptive encounter-level percentage, not a patient-level risk estimate or evidence that age caused readmission.

See [findings and limitations](../docs/FINDINGS_AND_LIMITATIONS.md) for the interpretation and [dataset notes](../docs/DATA_SOURCE.md) for the source.
