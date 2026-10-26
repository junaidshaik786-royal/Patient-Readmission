# SQL analysis: reproducible companion

These queries were prepared for this portfolio based on the public UCI dataset and original course screenshots. They are not presented as the exact original course-submitted SQL.

1. Download the official `diabetic_data.csv` from [UCI](../docs/DATA_SOURCE.md).
2. Load it in MySQL 8 as table `healthcare.diabetic_data` using MySQL Workbench's table data import wizard (keep original column names).
3. Run [02_readmission_analysis.sql](02_readmission_analysis.sql).

**Expected reconciliation:** 101,766 encounters, 71,518 distinct patients, 11,357 early-readmission-labelled encounters.

Do not present these descriptive associations as clinical predictions.
