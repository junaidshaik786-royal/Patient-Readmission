# Power BI dashboard

This is the existing Power BI report for the patient readmission analysis. The PBIX and visuals are unchanged; this page explains what is in the report and how to interpret it.

**Report file:** [Readmission Analysis Dashboard - Copy.pbix](Readmission%20Analysis%20Dashboard%20-%20Copy.pbix)

Open the file in Power BI Desktop to review the visuals.

## What's on the page

The report contains six visuals:

- Average clinical measures by recorded readmission status.
- Readmission breakdown by diagnosis count.
- Medication and lab-procedure pattern by readmission status.
- Encounter count by age band and readmission status.
- Encounter count by emergency-visit bucket.
- Average length of stay by primary diagnosis code.

## How to read it

- `<30` means the source records a readmission within 30 days.
- `>30` means a readmission after 30 days.
- `NO` means no readmission is recorded.
- Values are encounter counts, not unique-patient counts. One patient can appear in multiple rows.
- The clinical-measures chart combines different units on one shared scale. It is left as supplied in the original report, so compare those bar heights cautiously.

## Scope

This dashboard is descriptive and uses historical U.S. hospital encounter data from 1999–2008. It does not estimate an individual's risk, establish causation, or represent current hospital performance.

For the business question, KPI definitions, and data limitations, see the [project README](../README.md), [BRD](../docs/BRD.md), and [findings and limitations](../docs/FINDINGS_AND_LIMITATIONS.md).
