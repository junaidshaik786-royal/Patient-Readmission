# Requirements-to-evidence traceability

This maps the revised portfolio BRD to the artifacts available in the repository. It is not a hospital-approved traceability matrix.

| Requirement | Evidence | Status / qualification |
|---|---|---|
| BR-01 — Encounter counts and early-readmission KPI | `outputs/verified_metrics.json`; original evidence report, pp. 2–4 and 9 | Recalculated from the supplied CSV |
| BR-02 — Separate readmission labels | `sql/02_readmission_analysis.sql`; evidence report, pp. 3–4 | Counts and percentages use encounter records |
| BR-03 — Compare age, diagnosis and utilization groups | `outputs/age_group_readmission_rates.csv`; SQL/Excel screenshots; evidence report, pp. 4–8 and 10–13 | Descriptive, unadjusted comparisons |
| BR-04 — Dashboard view | Power BI screenshot; evidence report, pp. 9–12 | Screenshot evidence exists; report file is separately supplied by the candidate |
| BR-05 — Document data quality and limits | KPI dictionary, findings and source notes | Documents missingness, source period and encounter-versus-patient distinction |

## Scope boundary

The original course BRD includes proposed targets and estimated benefits. They are not measured outcomes. The project does not represent real hospital stakeholder approval, a clinical intervention, model validation, production deployment or realized ROI.
