# Patient Readmission Analytics
**Healthcare Business Analysis capstone | SQL · Excel · Power BI**

I used a public dataset of hospital encounters involving people with diabetes to explore one question: **what does the historical data show about readmissions within 30 days, and how could a reporting dashboard help a healthcare operations team investigate the pattern?**

The coursework included a Business Requirements Document (BRD), SQL and Excel analysis, and a Power BI dashboard. I have added reproducible validation code and supporting documentation so the calculations and assumptions are easier to review.

## At a glance

| Measure | Result |
|---|---:|
| Hospital encounters | **101,766** |
| Distinct patient IDs | **71,518** |
| Encounters labelled readmitted within 30 days (`<30`) | **11,357** |
| Within-30-day readmission proportion per encounter | **11.16%** |
| Average hospital stay | **4.40 days** |
| Average medications per encounter | **16.02** |

**Denominator note:** a person can appear in more than one encounter. The 11.16% is the share of encounter records labelled `<30`, not the share of unique patients and not a prediction of an individual's risk.

## Dashboard preview

![Patient Readmission Analytics Power BI dashboard](https://github.com/user-attachments/assets/6ab2d441-ec97-4386-959b-6da4341d1cc0)

[Dashboard and analysis screenshots](assets/README.md) · [Original coursework evidence report (PDF)](evidence/Patient_Readmission_Evidence_Report.pdf) · [Original coursework BRD (PDF)](evidence/Patient_Readmission_Original_BRD.pdf)

## What I worked on

- **Requirements:** documented the business question, scope, reporting needs, stakeholder roles in the course scenario, KPIs and business rules.
- **Analysis:** compared readmission labels, age bands, diagnoses and hospital-utilization measures.
- **Reporting:** reviewed SQL/Excel summaries and built a one-page Power BI dashboard.
- **Validation:** recalculated headline figures from the supplied CSV and checked the SQL queries against the same data.
- **Documentation:** recorded metric definitions, data-quality concerns, limitations and links between requirements and evidence.

The Python validator and SQL files in this repository are reproducibility companions prepared while organizing the portfolio. They are not represented as exact copies of the original coursework scripts.

## What stood out

- **11.16%** of encounter records carry the `<30` label; **34.93%** carry the `>30` label.
- In the `[20-30)` age band, **236 of 1,657 encounters (14.24%)** carry the `<30` label. This is an unadjusted comparison; it does not explain why the outcome occurred.
- Missing values are common in `weight` (**96.86%**), `medical_specialty` (**49.08%**) and `payer_code` (**39.56%**). Those fields need care before drawing conclusions from segmented charts.

One dashboard improvement I would make next is to separate the average-measures chart. Medications, procedures, diagnoses and hospital days use different units, so showing their averages on a shared scale can make comparisons harder to interpret.

## Project files

- [Business Requirements Document](docs/BRD.md)
- [KPI definitions and calculation rules](docs/KPI_DICTIONARY.md)
- [SQL queries](sql/02_readmission_analysis.sql) and [table schema](sql/01_schema.sql)
- [SQL setup guide](sql/README.md)
- [Data source and reproducibility notes](docs/DATA_SOURCE.md)
- [Findings and limitations](docs/FINDINGS_AND_LIMITATIONS.md)
- [Requirements-to-evidence traceability](docs/TRACEABILITY.md)
- [Verified metrics](outputs/verified_metrics.json) and [age-band summary](outputs/age_group_readmission_rates.csv)
- [Validation script](scripts/validate_metrics.py) and [automated tests](tests/test_validate_metrics.py)
- [Validation report](docs/VALIDATION_REPORT.md)
- [Lessons learned and next iteration](docs/LESSONS_LEARNED.md)

## Reproduce the numbers

1. Download `diabetic_data.csv` from the [UCI dataset page](https://archive.ics.uci.edu/dataset/296/diabetes+130-us-hospitals-for-years-1999-2008).
2. Run `python scripts/validate_metrics.py /path/to/diabetic_data.csv`.
3. Run `python -m unittest discover -s tests -v`.
4. Follow the [SQL setup guide](sql/README.md) to import the CSV into MySQL 8 and run the queries.

The source CSV used for validation contained 101,766 encounter rows and 50 columns. The raw patient-level dataset is not included here; only aggregate outputs are published.

## Scope and limitations

This is an **academic portfolio project**, not paid work for a hospital. The source covers U.S. hospital encounters from **1999–2008**. The analysis is descriptive: I did not build or validate a clinical prediction model, deploy a hospital workflow, or measure a reduction in readmissions or financial savings. The original course brief contains proposed targets; they were not achieved or independently verified.

**Dataset:** Clore, Cios, DeShazo and Strack (2014), *Diabetes 130-US Hospitals for Years 1999–2008*, [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/296/diabetes+130-us-hospitals-for-years-1999-2008), [DOI 10.24432/C5230J](https://doi.org/10.24432/C5230J).
