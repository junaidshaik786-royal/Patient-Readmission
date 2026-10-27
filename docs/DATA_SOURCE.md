# Dataset Provenance and Reproduction

**Primary source:** [UCI Diabetes 130-US Hospitals for Years 1999–2008](https://archive.ics.uci.edu/dataset/296/diabetes+130-us-hospitals-for-years-1999-2008)

**DOI:** https://doi.org/10.24432/C5230J

**Attribution:** Clore, J., Cios, K., DeShazo, J., & Strack, B. (2014). *Diabetes 130-US Hospitals for Years 1999–2008*, UCI Machine Learning Repository.

## Reviewed source

- Input file: `diabetic_data.csv`
- File size: 19,159,383 bytes
- SHA-256: `0689e7ec031237dc63031b938805c48377748761a3b26acab621567afa24df97`
- Rows: 101,766
- Columns: 50
- Distinct patient IDs: 71,518

## Important fields

- `encounter_id`: identifier for an encounter.
- `patient_nbr`: identifier for a patient; it may appear in multiple rows.
- `readmitted`: the recorded outcome categories `NO`, `>30` or `<30`.
- `age`: pre-grouped age bands, not exact ages.
- `time_in_hospital`: inpatient stay in days.
- `num_medications`, `num_lab_procedures`: counts recorded during an encounter.
- `weight`, `payer_code` and `medical_specialty`: contain substantial missingness encoded as `?`.

## Reproduce with MySQL Workbench

1. Download the CSV from the [UCI dataset page](https://archive.ics.uci.edu/dataset/296/diabetes+130-us-hospitals-for-years-1999-2008).
2. Open and run [`01_schema.sql`](../sql/01_schema.sql) to create the database and table.
3. Use the Table Data Import Wizard to import the full CSV into `healthcare.diabetic_data`. Map the CSV headers to the existing table columns and retain `?` values so missingness can be checked.
4. Open and run [`02_readmission_analysis.sql`](../sql/02_readmission_analysis.sql).
5. Compare headline figures with the [KPI dictionary](KPI_DICTIONARY.md) and [SQL run notes](../sql/README.md).

The workflow documented for this project is MySQL. No separate Python validation script is part of the published workflow.

## Scope, ethics and credit

These are historical U.S. hospital encounter records from 1999–2008. Their characteristics and collection methods may not represent present-day healthcare. Public project outputs are aggregates; the raw patient-level CSV is not republished. The project does not use hospital clients, real stakeholders or production clinical records.