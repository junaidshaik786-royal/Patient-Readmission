# Power BI dashboard

This is the Power BI report included with my patient readmission project. I have kept the uploaded PBIX and its visuals unchanged; this page explains what is in the report and how I interpret it.

**Report file:** [Readmission Analysis Dashboard - Copy.pbix](Readmission%20Analysis%20Dashboard%20-%20Copy.pbix)

Open the file in Power BI Desktop to inspect the report.

## What's on the page

The report contains six visuals:

- Average clinical measures by recorded readmission status.
- Readmission breakdown by diagnosis count.
- Medication and lab-procedure pattern, split by readmission status.
- Encounter count by age band and readmission status.
- Encounter count by emergency-visit bucket.
- Average length of stay by primary diagnosis code.

## How to read it

- `<30` means the source records a readmission within 30 days.
- `>30` means a readmission after 30 days.
- `NO` means no readmission is recorded in that field.
- Counts are encounter counts, not unique-patient counts. A patient can appear in multiple rows.
- The clinical-measures chart puts averages with different units on one shared scale. It is part of the existing report, so I have left it as supplied; be careful not to compare those bar heights as if all measures used the same unit.

## Scope

The dashboard is descriptive and uses historical U.S. hospital encounter data from 1999–2008. It does not estimate an individual's risk, establish that a factor caused readmission, or demonstrate a change in hospital performance.

For the business question, KPI definitions and data limitations, see the [project README](../README.md), [BRD](../docs/BRD.md), and [findings and limitations](../docs/FINDINGS_AND_LIMITATIONS.md).
