# Power BI report

The report supplied with this project contains one dashboard page with six analytical visuals and two text boxes.

## How to read it

- The `<30` label means the source dataset records a readmission within 30 days.
- Counts refer to encounters; a patient may appear in multiple rows.
- Charts are descriptive comparisons of historical data, not an individual risk prediction.
- The average-measures chart combines different units (for example, medications and hospital days) on a shared scale. A next iteration should split those measures into separate visuals or small multiples.

## File and verification

The editable `.pbix` should be added to this folder as `Patient_Readmission_Analytics.pbix`. The current report file supplied by the candidate passed archive-integrity and report-definition JSON checks, but it was not opened in Power BI Desktop in this environment. Data refresh and visual interactions therefore remain unverified.

See [data source notes](../docs/DATA_SOURCE.md) and [findings and limitations](../docs/FINDINGS_AND_LIMITATIONS.md).
