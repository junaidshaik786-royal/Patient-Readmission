# Business Requirements Document (BRD)
**Project:** 30-Day Patient Readmission Analytics Dashboard
**Type:** Revised academic portfolio requirements document
**Status:** Academic case study; not hospital-approved
**Dataset:** UCI Diabetes 130-US Hospitals, 1999–2008

## Business problem
Healthcare operations teams benefit from clear descriptive analysis of historical readmission patterns. This capstone considers how encounter-level reporting can support discussion about follow-up priorities, without predicting any individual's readmission or directing care.

## Objective and scope
**Objectives:** define early readmission KPIs; compare historical readmission patterns by age, diagnoses and utilization; build descriptive reports; document data quality; communicate questions for hypothetical stakeholders.

**In scope:** public de-identified historical encounter data, SQL / Excel summaries, Power BI evidence, requirements and dashboard traceability, KPI definitions.

**Out of scope:** hospital deployment, EHR integration, live health records, clinical decisions, predictive model validation, measured ROI, reduction in readmissions and stakeholder sign-off.

## Scenario stakeholders
| Role | Information need | Evidence boundary |
|---|---|---|
| Hospital operations lead | Aggregated trends and resource-planning discussions | No actual hospital involvement |
| Clinical reviewer | Descriptive patterns, discharge-follow-up questions | No clinical validation |
| Compliance reviewer | Data handling, provenance and limitations | No compliance certification |
| Business analyst | Problem, requirements, business rules, KPIs | Academic role |
| BI analyst | Query outputs and dashboard visualization | Original evidence is screenshots |

## Prioritized business requirements
| ID | Priority | Requirement | Acceptance criteria |
|---|---|---|---|
| BR-01 | High | Calculate encounter counts, unique patients and early-readmission KPI | 101,766 encounters; 71,518 patients; 11,357 early readmissions |
| BR-02 | High | Report all three readmission categories | Categories NO, >30 and <30 have consistent denominator |
| BR-03 | High | Compare age, diagnosis and utilization distributions | Counts and rates presented without causal claims |
| BR-04 | High | Present findings in a usable dashboard | Course screenshot evidence demonstrates Power BI visuals |
| BR-05 | High | Record source, missingness and interpretation limitations | Distinguish encounters from patients; disclose historical scope and missing fields |

## Business rules
- BRULE-01: A row is an encounter, while patient_nbr identifies a patient and can repeat.
- BRULE-02: Only the readmitted '<30' label counts as early readmission.
- BRULE-03: Early-readmission encounter proportion = number of <30 rows / number of selected encounter rows.
- BRULE-04: 'NO' and '>30' are separate categories.
- BRULE-05: '?' in source categorical fields signals missingness.
- BRULE-06: Descriptive patterns do not establish causation or clinical risk prediction.

## Non-functional expectations
- **Integrity:** reproduce headline KPIs from the source file.
- **Traceability:** connect requirement, KPI and output.
- **Usability:** show both counts and percentages for subgroup comparisons.
- **Privacy:** do not publish patient-level records.
- **Transparency:** label source period and methodological limitations.

## Risks and exclusions
The data are historical and substantially incomplete for some fields; repeated encounters can distort patient-level interpretations. All operational actions would require contemporary data, clinician evaluation and a separate implementation project.

## Business value statement
This capstone demonstrates how analysts can structure healthcare reporting questions and deliver descriptive insights. It does **not** substantiate the hypothetical 40% reporting-effort reduction, 95% accuracy or 320% ROI proposed in the original assignment.

Source: https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008
