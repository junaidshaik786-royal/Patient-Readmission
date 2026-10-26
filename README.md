# Patient Readmission Analytics
**Healthcare Business Analysis Capstone | SQL · Excel · Power BI**

## Why I worked on this

For my Business Analysis coursework, I worked with a public dataset of hospital encounters involving people with diabetes. The question was simple: **what can the data tell us about readmissions within 30 days, and how could a hospital team use those trends to ask better questions?**

I approached it as a reporting and business-analysis project, not a medical prediction system. I prepared a Business Requirements Document (BRD), explored the records with SQL and Excel, and built Power BI visuals to bring the findings together.

## What I did

1. **Defined the problem.** My BRD set out the objective, scope, stakeholder roles, requirements and intended dashboard outputs.
2. **Explored the data.** I used SQL to look at readmission categories, age groups, diagnoses, medication counts and hospital stays. I also created Excel summaries.
3. **Built the reporting view.** The course evidence report contains screenshots of my SQL results, Excel work and Power BI dashboard.
4. **Interpreted the results.** I focused on what the figures show, what they do not show, and which areas would deserve further investigation.

## Key results

| What I measured | Result |
|---|---:|
| Hospital encounters | **101,766** |
| Unique patients in the dataset | **71,518** |
| Encounters followed by a recorded readmission within 30 days | **11,357** |
| **30-day readmission proportion (per encounter)** | **11.16%** |
| Average hospital stay | **4.40 days** |
| Average medications recorded per encounter | **16.02** |

I checked the totals against the supplied CSV. An important distinction is that **101,766 refers to encounters, not separate patients**: one patient may appear more than once. The 11.16% figure is an encounter-level measure.

## What stood out to me

- The dataset labels **11.16%** of encounters as readmitted in under 30 days. Another **34.93%** are labeled as readmitted after 30 days.
- In the **20–30 age group**, **236 of 1,657 encounters (14.24%)** have the under-30-day label. That's worth looking into, but it does not prove that age caused the difference.
- Several fields have a lot of missing information: **weight (96.86%)**, **medical specialty (49.08%)** and **payer code (39.56%)**. I would be careful about making decisions from those columns without first reviewing the data quality.

My main takeaway was that **getting the definition and denominator right matters as much as making the chart**. A useful dashboard should make patterns easier to investigate, not make unsupported claims.

## My work and supporting files

| File | What's inside |
|---|---|
| [Business Requirements Document](docs/BRD.md) | Project objective, scope, stakeholder roles and five reporting requirements |
| [KPI Definitions](docs/KPI_DICTIONARY.md) | Calculations and rules used to interpret the numbers |
| [SQL queries](sql/02_readmission_analysis.sql) | Query logic for counts, readmissions, age groups and other measures |
| [Data source and quality notes](docs/DATA_SOURCE.md) | Dataset details, missing values and source attribution |
| [Analysis findings](docs/FINDINGS_AND_LIMITATIONS.md) | What I found and what I would investigate next |
| [Requirements and evidence map](docs/TRACEABILITY.md) | How the analytical outputs relate to the requirements |
| [Verified results](outputs/verified_metrics.json) | Headline counts checked against the source CSV |

**Original coursework evidence:** I also prepared a screenshot report containing SQL, Excel and Power BI outputs. Its PDF and a few dashboard screenshots are **not uploaded to this repository yet**; I will link them here once they're available. The SQL and Python files published here include additional reproducibility material prepared while organizing the portfolio; they are not claimed to be the original course-submitted source files.

## What I would improve next

With more time, I'd strengthen the dashboard by showing the encounter count alongside every subgroup percentage, adding clearer notes for missing fields, and testing the reports with sample user questions. In a real hospital project, I'd also need current data, clinical input and agreed definitions before anyone acted on a finding.

## Project context

This was an **academic capstone**, not paid work for a hospital or a live healthcare implementation. The course used a fictional scenario organization. I did not develop a validated prediction model or measure an actual reduction in readmissions.

**Dataset:** [UCI Diabetes 130-US Hospitals for Years 1999–2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008) · [DOI 10.24432/C5230J](https://doi.org/10.24432/C5230J). Data are historical, so these findings should not be assumed to describe today's hospitals.
