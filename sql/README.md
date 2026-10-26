# SQL analysis

These MySQL 8 query files were prepared as reproducibility companions for this portfolio. They are not represented as byte-for-byte copies of the original coursework SQL.

## Run the analysis

1. Download `diabetic_data.csv` from the [UCI dataset page](../docs/DATA_SOURCE.md).
2. In MySQL Workbench, run [`01_schema.sql`](01_schema.sql) to create `healthcare.diabetic_data`.
3. Use **Table Data Import Wizard** to import the CSV, mapping the header row to the existing columns. Keep `?` values so missingness can be measured.
4. Run [`02_readmission_analysis.sql`](02_readmission_analysis.sql).

The first query should return **101,766 encounters**, **71,518 distinct patient IDs**, **11,357 `<30` encounters**, and an **11.16%** encounter-level proportion.

## Validation status

All nine SELECT queries were executed against the supplied 101,766-row CSV loaded into SQLite, after removing the MySQL-specific `USE healthcare;` statement. The results reconciled with the Python validator. A MySQL server was not available in this environment, so MySQL Workbench import and execution still need a local run.

The raw patient-level CSV, credentials and local file paths are not included in the repository.
