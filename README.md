# Patient Readmission Analytics
### Healthcare Business Analysis | 30-Day Readmission Dashboard

**Independent academic capstone** · Business Requirements · SQL · Excel · Power BI · Healthcare Operations Reporting

> **Portfolio disclosure:** This project was completed as an academic exercise using the public UCI Diabetes 130-US Hospitals dataset (1999–2008). It is **not** a real hospital implementation or paid engagement. ReadmitGuard Analytics and named stakeholders belong to the course scenario. No deployed risk-prediction model, clinical validation, cost savings, or reduction in readmissions is claimed.

## Business problem
Can historical hospital encounter data reveal useful patterns in **30-day readmissions** that a healthcare operations team could investigate when planning follow-up care and reporting improvements?

**BA approach:** Business question → BRD and scope → Requirements and KPIs → Data checks → SQL/Excel analysis → Power BI dashboard → Decision-support findings.

## Verified results
The following figures were recalculated from the submitted `diabetic_data.csv` (each row is a hospital **encounter**, not necessarily a distinct patient).

| Metric | Result | Interpretation |
| --- | ---: | --- |
| Total hospital encounters | **101,766** | Source records |
| Unique patients | **71,518** | Distinct `patient_nbr` identifiers |
| Readmitted in under 30 days | **11,357** | Encounters labeled `<30` |
| **30-day readmission proportion** | **11.16%** | 11,357 / 101,766 encounters |
| Readmitted after 30 days | **35,545** | Encounters labeled `>30` |
| No recorded readmission | **54,864** | Encounters labeled `NO` |
| Average hospital stay | **4.40 days** | Encounter-level average |
| Average medications | **16.02** | Encounter-level average |

**Important:** The 11.16% figure is descriptive and encounter-based. It is not the proportion of distinct patients readmitted, nor a predictive model's accuracy.

## Business Analysis deliverables
- [**Revised Business Requirements Document**](docs/BRD.md): problem statement, scope, academic stakeholder roles, five requirements, business rules and acceptance criteria.
- [**KPI Dictionary**](docs/KPI_DICTIONARY.md): metric formulas, reporting grain and data-quality expectations.
- [**Requirements-to-Evidence Traceability**](docs/TRACEABILITY.md): connects requirements to the coursework screenshots and reproducible outputs.
- [**Findings and Limitations**](docs/FINDINGS_AND_LIMITATIONS.md): descriptive findings and recommendations appropriate for further clinical investigation.
- [**Data Source and Provenance**](docs/DATA_SOURCE.md): source, caveats and reproducibility instructions.
- [**SQL Analysis**](sql/02_readmission_analysis.sql): queries for counts, outcomes, age bands, diagnoses, admission types and missingness.
- [**Python Verification Companion**](scripts/validate_metrics.py): calculates headline results from the source CSV.
- [**Validated Summary**](outputs/verified_metrics.json) and [**Age-Band Results**](outputs/age_group_readmission_rates.csv): inspectable, aggregate outputs.

**Evidence clarification:** The academic submission included a BRD PDF and a 14-page screenshot evidence report showing SQL, Excel and Power BI outputs. The repository's original PDFs and screenshot images will be linked after they have been uploaded and confirmed. The SQL and Python files here are newly prepared **reproducibility companions**, not byte-for-byte copies of the course-submitted scripts; an editable original `.pbix` and original SQL/Excel source files were not supplied.

## Key findings
1. **11.16%** of encounter records were labeled as a readmission in under 30 days.
2. In the **20–30 age band**, 236 of 1,657 encounters (**14.24%**) carried that label. This is an unadjusted historical association, **not** a causal result or clinical risk score.
3. The source contains substantial missingness: `weight` **96.86%**, `medical_specialty` **49.08%**, `payer_code` **39.56%**.
4. These records are from **1999–2008** and must not be assumed to represent contemporary hospital practice.

**Operational recommendation:** Use the descriptive dashboard to identify questions for clinical and quality teams, review missing data before relying on payer/specialty comparisons, and evaluate any prospective intervention only with appropriate clinical validation.

## Reproduce the figures
1. Obtain the original CSV from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008).
2. Run `python scripts/validate_metrics.py /path/to/diabetic_data.csv`.
3. See [SQL setup guidance](sql/README.md) for optional MySQL 8 queries.

**Dataset credit:** Clore, Cios, DeShazo and Strack (2014), *Diabetes 130-US Hospitals for Years 1999–2008*, UCI Machine Learning Repository, [DOI: 10.24432/C5230J](https://doi.org/10.24432/C5230J).

This repository contains no patient-level CSV export, hospital client records or database credentials. No stakeholder approval, HIPAA certification, EHR integration, predictive performance, realized ROI or patient-outcome improvements are represented.
