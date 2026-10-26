# Patient Readmission Analysis

**Business Analysis portfolio project | Healthcare | SQL, Excel and Power BI**

## Project

This coursework project looks at readmission records in the UCI Diabetes 130-US Hospitals dataset. The aim was to summarize how often an encounter was followed by a readmission within 30 days and compare the recorded outcomes across age groups and other encounter measures.

The project includes a business requirements document, SQL analysis, Excel work, a Power BI dashboard and the original course evidence.

## Dashboard

![Patient Readmission dashboard](https://github.com/user-attachments/assets/6ab2d441-ec97-4386-959b-6da4341d1cc0)

[Power BI report file](dashboard/Readmission%20Analysis%20Dashboard%20-%20Copy.pbix) · [Dashboard and analysis screenshots](assets/README.md) · [Course evidence report (PDF)](evidence/Patient_Readmission_Evidence_Report.pdf)

## Main results

| Measure | Result |
|---|---:|
| Encounter records | 101,766 |
| Distinct patient IDs | 71,518 |
| Encounters labelled `<30` | 11,357 |
| `<30` as a share of all encounters | 11.16% |
| Encounters labelled `>30` | 35,545 |
| Encounters labelled `NO` | 54,864 |

The denominator is important: one patient can have multiple encounters. The 11.16% figure is an encounter-level proportion, not the percentage of unique patients who were readmitted.

## What is in this repository?

- [Business requirements document](docs/BRD.md) — problem, scope, requirements and acceptance criteria.
- [KPI definitions](docs/KPI_DICTIONARY.md) — metric definitions and denominator rules.
- [SQL schema and queries](sql/01_schema.sql) and [analysis queries](sql/02_readmission_analysis.sql).
- [SQL setup notes](sql/README.md).
- [Findings and limitations](docs/FINDINGS_AND_LIMITATIONS.md).
- [Source and data notes](docs/DATA_SOURCE.md).
- [Age-group results](outputs/age_group_readmission_rates.csv).
- [Original course BRD](evidence/Patient_Readmission_Original_BRD.pdf).

## Findings worth discussing

- 11.16% of encounter records have the `<30` label; 34.93% have the `>30` label.
- In the `[20-30)` age band, 236 of 1,657 encounters (14.24%) have the `<30` label.
- Weight is missing for 96.86% of records, medical specialty for 49.08%, and payer code for 39.56%.

These are descriptive results from historical data. They do not show that age or another factor caused readmission.

## Limitations

The dataset covers U.S. hospital encounters from 1999–2008, so it should not be treated as a picture of current hospital performance. This is an academic project, not work for a hospital. No clinical prediction model was validated, and no reduction in readmissions, cost savings or other operational benefit was measured. Targets in the original course brief are proposed targets, not achieved results.

**Dataset:** [UCI Diabetes 130-US Hospitals for Years 1999–2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us-hospitals+for+years+1999-2008).
