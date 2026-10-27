# Patient Readmission Analysis

This is a healthcare analysis project I completed as coursework and am using in my Business Analyst portfolio. I used the UCI Diabetes 130-US Hospitals dataset (1999–2008) to look at recorded readmission outcomes and compare patterns across age groups, diagnosis counts and a few measures of hospital use.

I wanted the work to be reviewable beyond the dashboard, so I have included the business requirements, KPI definitions, data-source notes, SQL scripts, findings and original coursework evidence.

## Dashboard

![Patient Readmission dashboard built in Power BI](https://github.com/user-attachments/assets/9ab922c6-2eb8-4a04-9413-cf45903186ed)

[Open the Power BI file](dashboard/Readmission%20Analysis%20Dashboard%20-%20Copy.pbix) · [Read the dashboard notes](dashboard/README.md)

## What I worked on

- Set out the business question, scope and rules in a Business Requirements Document (BRD).
- Used MySQL queries to summarize readmission categories, age bands, diagnosis codes, hospital use and missing values.
- Documented the KPIs and how their denominators are counted.
- Used Power BI to bring the comparisons together in one report.
- Recorded the main findings and the limits of what this historical dataset can tell us.

## A few results

| Measure | Result |
|---|---:|
| Encounter records | 101,766 |
| Distinct patient IDs | 71,518 |
| Encounters labelled `<30` | 11,357 (11.16%) |
| Encounters labelled `>30` | 35,545 (34.93%) |
| Encounters labelled `NO` | 54,864 (53.91%) |
| Encounters aged 20–30 labelled `<30` | 236 of 1,657 (14.24%) |

One detail matters when reading these numbers: a patient can have more than one encounter. The 11.16% figure is the share of encounter records labelled `<30`, not the percentage of unique patients readmitted within 30 days.

The source also has substantial missingness in some fields: weight is missing in 96.86% of records, medical specialty in 49.08%, and payer code in 39.56%. I kept that in mind when interpreting the results.

## Explore the project

- [Project documentation](docs/README.md) — an introduction to the BRD, KPI dictionary, source notes, and findings.
- [Business Requirements Document](docs/BRD.md) — the question, scope, requirements and business rules.
- [KPI dictionary](docs/KPI_DICTIONARY.md) — definitions and counting rules for the measures.
- [Dataset notes](docs/DATA_SOURCE.md) — source, fields, provenance and reproducibility details.
- [Findings and limitations](docs/FINDINGS_AND_LIMITATIONS.md) — what stood out and what I would check next.
- [Power BI report notes](dashboard/README.md) — what the existing dashboard contains and how to read it.
- [MySQL scripts and run instructions](sql/README.md) — database setup, CSV import and analysis queries.
- [Age-band output](outputs/README.md) — notes on the aggregated CSV result.
- [Original coursework evidence](evidence/README.md) — the evidence report and original BRD.

## Limitations

The records cover U.S. hospital encounters from 1999–2008, so they are not a picture of current hospital performance. This is an academic portfolio project, not a hospital deployment. I did not build or validate a clinical prediction model, establish causes of readmission, or measure improvements in hospital outcomes or cost. Targets in the original coursework brief are proposed targets, not achieved results.

**Dataset:** [UCI Diabetes 130-US Hospitals for Years 1999–2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us-hospitals+for-years-1999-2008).
