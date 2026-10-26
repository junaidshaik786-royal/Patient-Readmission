-- MySQL 8 descriptive analytics companion, not the original coursework SQL.
-- Import official UCI diabetic_data.csv into healthcare.diabetic_data.
USE healthcare;
-- 1. Reconcile total encounters, unique patients, early readmissions and average stay.
SELECT COUNT(*) AS encounters,
 COUNT(DISTINCT patient_nbr) AS unique_patients,
 SUM(CASE WHEN readmitted = '<30' THEN 1 ELSE 0 END) AS readmitted_lt30,
 ROUND(100.0*SUM(CASE WHEN readmitted = '<30' THEN 1 ELSE 0 END)/COUNT(*),2) AS readmit_lt30_pct,
 ROUND(AVG(time_in_hospital),2) AS mean_hospital_days,
 ROUND(AVG(num_medications),2) AS mean_medications
FROM diabetic_data;
-- 2. All readmission categories.
SELECT readmitted,COUNT(*) AS encounters,
 ROUND(100.0*COUNT(*)/(SELECT COUNT(*) FROM diabetic_data),2) AS percent_of_encounters
FROM diabetic_data GROUP BY readmitted ORDER BY encounters DESC;
-- 3. Age-band comparisons: counts AND unadjusted proportions.
SELECT age,COUNT(*) AS encounters,
 SUM(CASE WHEN readmitted = '<30' THEN 1 ELSE 0 END) AS readmitted_lt30,
 ROUND(100.0*SUM(CASE WHEN readmitted = '<30' THEN 1 ELSE 0 END)/COUNT(*),2) AS rate_lt30_pct
FROM diabetic_data GROUP BY age ORDER BY age;
-- 4. Primary diagnosis code frequencies.
SELECT diag_1 AS diagnosis_code,COUNT(*) AS encounters
FROM diabetic_data WHERE diag_1 <> '?' AND diag_1 <> '' AND diag_1 IS NOT NULL
GROUP BY diag_1 ORDER BY encounters DESC LIMIT 10;
-- 5. Admission types and mean length of stay.
SELECT admission_type_id,COUNT(*) AS encounters,
 ROUND(AVG(time_in_hospital),2) AS mean_stay_days
FROM diabetic_data GROUP BY admission_type_id ORDER BY encounters DESC;
-- 6. Previous inpatient utilization and recorded early readmission.
SELECT number_inpatient,COUNT(*) AS encounters,
 ROUND(100.0*SUM(CASE WHEN readmitted='<30' THEN 1 ELSE 0 END)/COUNT(*),2) AS rate_lt30_pct
FROM diabetic_data GROUP BY number_inpatient ORDER BY number_inpatient;
-- 7. Categorical missingness.
SELECT COUNT(*) AS total,
 SUM(CASE WHEN weight='?' OR weight IS NULL OR weight='' THEN 1 ELSE 0 END) AS weight_missing,
 SUM(CASE WHEN medical_specialty='?' OR medical_specialty IS NULL OR medical_specialty='' THEN 1 ELSE 0 END) AS specialty_missing,
 SUM(CASE WHEN payer_code='?' OR payer_code IS NULL OR payer_code='' THEN 1 ELSE 0 END) AS payer_missing
FROM diabetic_data;
