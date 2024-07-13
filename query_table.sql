
-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS healthcare_data;

-- Use the database
USE healthcare_data;

-- Create table for patient records with additional fields
DROP TABLE IF EXISTS patient_records;
CREATE TABLE patient_records (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    gender VARCHAR(10),
    diagnosis_date DATE,
    medical_history TEXT,
    visit_records TEXT,
    treatment_plan TEXT,
    outcome TEXT,
    date_of_birth DATE,
    contact_info VARCHAR(100),
    insurance_info VARCHAR(100),
    ethnicity VARCHAR(50),
    allergies TEXT
);

-- Create table for hospital data with additional fields
DROP TABLE IF EXISTS hospital_data;
CREATE TABLE hospital_data (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    department VARCHAR(100),
    bed_availability INT,
    doctors_available INT,
    equipment_status TEXT,
    staff_schedule TEXT,
    resource_utilization TEXT,
    avg_patient_wait_time TIME,
    admission_rate FLOAT,
    discharge_rate FLOAT,
    patient_satisfaction_score FLOAT
);

-- Create table for public health data with additional fields
DROP TABLE IF EXISTS public_health_data;
CREATE TABLE public_health_data (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    disease VARCHAR(100),
    geographic_region VARCHAR(100),
    health_trend TEXT,
    public_health_intervention TEXT,
    impact_on_operations TEXT,
    vaccination_rate FLOAT,
    healthcare_access TEXT,
    economic_impact TEXT
);

CREATE TABLE IF NOT EXISTS appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_name VARCHAR(100),
    appointment_date DATETIME,
    status VARCHAR(20),
    FOREIGN KEY (patient_id) REFERENCES patient_records(patient_id)
);