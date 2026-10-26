# Patient Readmission Analysis

This is a healthcare analysis project I completed as coursework and am using in my Business Analyst portfolio. I looked at readmission records in the UCI Diabetes 130-US Hospitals dataset and used SQL, Excel and Power BI to explore the results.

## Dashboard

![Patient Readmission dashboard](https://github.com/user-attachments/assets/6ab2d441-ec97-4386-959b-6da4341d1cc0)

[Open the Power BI file](dashboard/Readmission%20Analysis%20Dashboard%20-%20Copy.pbix) · [View the original coursework evidence](evidence/Patient_Readmission_Evidence_Report.pdf)

## A few results

| Measure | Result |
|---|---:|
| Encounter records | 101,766 |
| Distinct patient IDs | 71,518 |
| Encounters labelled `<30` | 11,357 |
| `<30` encounters as a share of all encounters | 11.16% |
| Encounters labelled `>30` | 35,545 |
| Encounters labelled `NO` | 54,864 |

One important detail: a patient can have more than one encounter. So, 11.16% is the share of encounter records labelled `<30`, not the percentage of unique patients readmitted within 30 days.

## Files

- [Business Requirements Document](docs/BRD.md) — the business question, scope, requirements and rules used for the analysis.
- [KPI definitions](docs/KPI_DICTIONARY.md) — what each measure means and how it is counted.
- [SQL queries](sql/02_readmission_analysis.sql) and [table setup](sql/01_schema.sql).
- [How to run the SQL](sql/README.md).
- [Findings and limitations](docs/FINDINGS_AND_LIMITATIONS.md).
- [Dataset notes](docs/DATA_SOURCE.md).
- [Age-band results](outputs/age_group_readmission_rates.csv).
- [Original course BRD](evidence/Patient_Readmission_Original_BRD.pdf).

## What I noticed

- 11.16% of encounter records have the `<30` label; 34.93% have the `>30` label.
- In the `[20-30)` age band, 236 of 1,657 encounters (14.24%) have the `<30` label.
- Weight is missing in 96.86% of records, medical specialty in 49.08%, and payer code in 39.56%.

These are patterns in the historical data, not proof that age or another factor caused readmission.

## Limitations

The dataset covers U.S. hospital encounters from 1999–2008, so it should not be treated as a picture of current hospital performance. This was an academic project, not work for a hospital. I did not build or validate a clinical prediction model, and I have not measured any reduction in readmissions or cost savings. Targets mentioned in the original course brief are proposed targets, not achieved results.

**Dataset:** [UCI Diabetes 130-US Hospitals for Years 1999–2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us-hospitals+for-years-1999-2008).
