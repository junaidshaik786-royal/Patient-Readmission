# Patient Readmission Analysis

**Business Analyst portfolio case study | MySQL · Power BI · Requirements and KPI definition**

I used the UCI Diabetes 130-US Hospitals dataset (1999–2008) to explore how recorded readmission outcomes vary across hospital encounters and selected patient/encounter groups. I treated this as a descriptive reporting problem: define the question, make the counting rules explicit, analyze the data in MySQL, and present the comparisons in the Power BI dashboard.

## Dashboard

![Preview of the existing Patient Readmission Analytics Dashboard](assets/patient-readmission-dashboard-preview.jpg)

The image above is a preview of my existing six-visual Power BI dashboard. **The PBIX and dashboard itself have not been changed.**

[Open the Power BI file](dashboard/Readmission%20Analysis%20Dashboard%20-%20Copy.pbix) · [Dashboard notes](dashboard/README.md)

## Business question

How are the recorded readmission outcomes distributed across encounters, and what descriptive patterns across age groups, diagnosis counts and hospital-use measures could help a healthcare operations team decide what to investigate further?

The dataset contains historical U.S. hospital encounter records from 1999–2008. It does not describe current hospital performance.

## KPI snapshot

| Measure | Result |
|---|---:|
| Encounter records | 101,766 |
| Distinct patient IDs | 71,518 |
| Encounters labelled `<30` | 11,357 (11.16%) |
| Encounters labelled `>30` | 35,545 (34.93%) |
| Encounters labelled `NO` | 54,864 (53.91%) |
| Encounters in the 20–30 age band labelled `<30` | 236 of 1,657 (14.24%) |

**Important denominator rule:** one row is an encounter; the same patient may appear in multiple rows. The 11.16% value is the proportion of encounter records labelled `<30`, not the percentage of unique patients who were readmitted within 30 days. The age-band percentage is also encounter-level and unadjusted.

## What I did

- Defined the business question and analytical scope, then documented the requirements and business rules in a Business Requirements Document (BRD).
- Defined the KPIs and their counting rules, including the distinction between encounter records and unique patient IDs.
- Used MySQL to summarize the readmission categories, age groups, diagnosis counts, hospital-use measures and missing values.
- Presented the comparisons in my existing Power BI dashboard.
- Recorded findings, source details, data-quality issues and limitations so the report can be reviewed beyond the visuals.

## What I learned

- **Grain and denominator come first.** Counting encounters is not the same as counting unique patients; percentages need an explicit denominator.
- **Missing data affects interpretation.** In this dataset, weight is missing in 96.86% of records, medical specialty in 49.08%, and payer code in 39.56%. That limits what can be responsibly concluded from those fields.
- **Descriptive patterns are not explanations.** Differences between groups do not prove what caused a readmission, establish an individual patient's risk, or validate a clinical prediction model.
- **A dashboard needs traceable definitions.** Requirements, KPI logic, SQL queries and limitations all matter alongside the visual presentation.

## What I would do next

Before considering a practical product or service, I would validate the real reporting problem with healthcare operations and quality stakeholders. I would ask which decisions the report should support, who uses it, how readmission is defined locally, what current and representative data are available, and what workflow, privacy and governance requirements apply. Only after confirming a genuine need would I define a small pilot and agree how its usefulness should be measured.

This is a proposed next step, not stakeholder work completed during this portfolio project.

## Explore the project

- [Business Requirements Document](docs/BRD.md) — business question, scope, requirements and business rules.
- [KPI dictionary](docs/KPI_DICTIONARY.md) — definitions and denominator rules.
- [Dataset provenance and MySQL reproduction notes](docs/DATA_SOURCE.md) — source, file fingerprint and workflow.
- [Findings and limitations](docs/FINDINGS_AND_LIMITATIONS.md) — descriptive results and follow-up questions.
- [Power BI dashboard notes](dashboard/README.md) — what the existing report contains.
- [MySQL scripts and run instructions](sql/README.md) — database setup and analysis queries.
- [Aggregated age-band output](outputs/README.md).
- [Original coursework evidence](evidence/README.md) — evidence report and original BRD.

## Limitations and disclosure

The dataset is historical (1999–2008), and its characteristics may not represent present-day hospitals. This is an academic portfolio case study, not a hospital deployment. I did not validate a clinical prediction model, establish causes of readmission, work with a real hospital stakeholder, or measure changes in hospital outcomes, workload or cost. Targets in the original coursework brief are proposed targets, not achieved results. The repository publishes aggregate outputs rather than republishing the patient-level CSV.

**Dataset:** [UCI Diabetes 130-US Hospitals for Years 1999–2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us-hospitals+for-years-1999-2008).