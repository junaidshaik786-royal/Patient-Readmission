# Validation report

**Run date:** 26 October 2026  
**Purpose:** check that the published aggregate metrics can be recalculated and that the validation script handles common input errors.

## Source-file check

The supplied `diabetic_data.csv` was checked using SHA-256:

`0689e7ec031237dc63031b938805c48377748761a3b26acab621567afa24df97`

The digest matches the reviewed source file.

## Recalculated headline results

| Check | Result |
|---|---:|
| Encounter rows | 101,766 |
| Distinct patient IDs | 71,518 |
| `<30` readmission label | 11,357 |
| `>30` readmission label | 35,545 |
| `NO` readmission label | 54,864 |
| `<30` share of encounter rows | 11.16% |
| Mean hospital stay | 4.40 days |
| Mean medications | 16.02 |
| Mean lab procedures | 43.10 |

## Automated tests

The local unit-test run passed **3 tests** covering aggregate calculation, duplicate patient IDs, missingness, required columns and empty input. The same tests are configured to run in GitHub Actions when the validation code or tests change.

## SQL checks

All nine SELECT queries in `sql/02_readmission_analysis.sql` were executed against the supplied CSV loaded into SQLite after removing the MySQL-specific `USE healthcare;` statement. The results reconciled with the Python metrics.

**Not yet verified:** the SQL was not executed on a live MySQL server in this environment, and the Power BI report was not opened in Power BI Desktop. Its PBIX archive and report-definition JSON were checked for integrity, but visual refresh and interactions were not independently tested.

These checks validate descriptive calculations only. They do not validate a clinical model or prove real-world healthcare outcomes.
