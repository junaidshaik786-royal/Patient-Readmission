# SQL analysis

I used these MySQL 8 scripts to set up the project table and explore the UCI hospital-encounter data in a database. They are reproducibility scripts for this portfolio, not byte-for-byte copies of the original coursework SQL.

## Files in this folder

- [`01_schema.sql`](01_schema.sql) creates the `healthcare` database and the `diabetic_data` table.
- [`02_readmission_analysis.sql`](02_readmission_analysis.sql) contains queries for the main counts, readmission categories, age bands, primary diagnosis codes, admission type, previous inpatient use and missing values.

## Run it in MySQL Workbench

1. Download `diabetic_data.csv` from the [UCI dataset page](../docs/DATA_SOURCE.md).
2. Open and run `01_schema.sql` to create the database and table.
3. Use **Table Data Import Wizard** to load the CSV into `healthcare.diabetic_data`. Map the CSV header to the existing columns and keep `?` values so missingness can be checked.
4. Open and run `02_readmission_analysis.sql`.

## Quick check

The summary query should return:

| Measure | Expected result |
|---|---:|
| Encounter records | 101,766 |
| Distinct patient IDs | 71,518 |
| Encounters labelled `<30` | 11,357 |
| `<30` encounters as a share of all encounters | 11.16% |

If the results differ, check that the full CSV was imported and that the header row was not loaded as data. Keep the distinction between encounters and unique patients: `encounter_id` identifies an encounter, while `patient_nbr` can repeat across encounters.

The queries are descriptive. They help summarize the recorded data; they do not establish why readmission happened or predict an individual patient's outcome. The raw patient-level CSV is not included in this repository.

See [dataset notes](../docs/DATA_SOURCE.md) and the [KPI dictionary](../docs/KPI_DICTIONARY.md) for definitions and source details.
