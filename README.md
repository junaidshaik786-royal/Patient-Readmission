# Patient Readmission Analytics
**Healthcare Business Analysis Capstone | SQL · Excel · Power BI**

## Project overview

For my Business Analysis coursework, I explored a public dataset of hospital encounters involving people with diabetes. I wanted to understand what the historical data showed about readmissions within 30 days and how a reporting view could help a healthcare operations team investigate the pattern.

I documented the business question and scope, defined the key measures, reviewed the data with SQL and Excel, and used Power BI visuals to summarize the results. This is an academic case study, not a live hospital implementation or a clinical prediction tool.

## What I worked on

- **Business requirements:** set out the objective, scope, stakeholders in the course scenario, reporting needs and acceptance criteria.
- **Data analysis:** reviewed readmission categories, age groups, diagnoses and hospital-utilization measures.
- **Reporting:** used SQL and Excel analysis and created a Power BI dashboard for comparing the recorded outcomes.
- **Interpretation:** documented the findings, data-quality concerns and questions that would need further investigation before any operational action.

## Key results

| Measure | Result |
|---|---:|
| Hospital encounters | **101,766** |
| Distinct patient IDs | **71,518** |
| Encounters labeled readmitted within 30 days | **11,357** |
| Within-30-day readmission proportion per encounter | **11.16%** |
| Average length of stay | **4.40 days** |
| Average medications per encounter | **16.02** |

The denominator matters: the dataset contains 101,766 encounter records, not 101,766 different people. The 11.16% is a descriptive encounter-level proportion, not an individual patient's predicted risk.

## Dashboard preview

The screenshot below is from the coursework dashboard. It shows comparisons by readmission category, age, diagnosis and hospital-utilization measures.

![Power BI Patient Readmission Analytics Dashboard](https://github.com/user-attachments/assets/6ab2d441-ec97-4386-959b-6da4341d1cc0)

[See the dashboard and analysis screenshots](assets/README.md)

## What stood out

- **11.16%** of encounters carry the dataset's `<30` readmission label; **34.93%** carry the `>30` label.
- In the 20–30 age band, **236 of 1,657 encounters (14.24%)** carry the `<30` label. This is an unadjusted comparison, not evidence that age caused the outcome.
- Missing values are substantial in some fields: weight (**96.86%**), medical specialty (**49.08%**) and payer code (**39.56%**). Those fields need caution before being used to draw conclusions.

My main learning was to check the meaning of a metric and its denominator before interpreting a chart. A dashboard can make a pattern easier to see, but it cannot explain the cause by itself.

## Project documents and evidence

| Artifact | What it contains |
|---|---|
| [Business Requirements Document](docs/BRD.md) | Project objective, scope, stakeholder roles, five requirements and acceptance criteria |
| [KPI Dictionary](docs/KPI_DICTIONARY.md) | Definitions, formulas and denominator rules |
| [SQL analysis queries](sql/02_readmission_analysis.sql) | Queries for counts, readmission categories, age groups and missingness |
| [SQL table schema](sql/01_schema.sql) | Source-aligned table structure for reproducing the queries |
| [Findings and limitations](docs/FINDINGS_AND_LIMITATIONS.md) | Results, interpretation and questions for further investigation |
| [Data source and quality notes](docs/DATA_SOURCE.md) | Dataset provenance, field notes and reproduction instructions |
| [Requirements traceability](docs/TRACEABILITY.md) | How requirements relate to evidence and outputs |
| [Verified metrics](outputs/verified_metrics.json) | Recomputed headline totals and data-quality checks |
| [Age-band summary](outputs/age_group_readmission_rates.csv) | Aggregated counts and encounter-level proportions |
| [Original course evidence report (PDF)](evidence/Patient_Readmission_Evidence_Report.pdf) | 14-page screenshot evidence report with SQL, Excel and Power BI outputs |
| [Original course BRD (PDF)](evidence/Patient_Readmission_Original_BRD.pdf) | Submitted coursework brief; contains proposed targets that were not measured results |

The SQL and Python validation files in this repository include reproducibility material prepared while organizing the portfolio. They are not represented as exact copies of the original course-submitted scripts. The editable Power BI `.pbix` file was not supplied.

## Findings and limitations

The source covers U.S. hospital encounters from **1999–2008**, so it should not be treated as a picture of current healthcare. Some patients have multiple encounters, several fields have extensive missing data, and the analysis is descriptive. I did not build or validate a predictive model, implement a hospital workflow, or measure a reduction in readmissions or financial savings.

For a real project, I would first confirm definitions and reporting needs with current business and clinical stakeholders, then validate data quality and review the findings with qualified clinical staff before proposing any intervention.

## Dataset

[UCI Diabetes 130-US Hospitals for Years 1999–2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us-hospitals+for+years+1999-2008) · [DOI 10.24432/C5230J](https://doi.org/10.24432/C5230J).

**Project type:** Academic Healthcare Business Analysis / Reporting Analytics capstone.
