import menu
from data_import import import_data
from data_preprocessing import preprocess_data
from data_insertion import insert_data
from db_config import create_connection

def setup_database():
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return
    
    # Create the necessary tables
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patient_records (
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
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hospital_data (
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
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS public_health_data (
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
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        appointment_id INT AUTO_INCREMENT PRIMARY KEY,
        patient_id INT,
        doctor_name VARCHAR(100),
        appointment_date DATETIME,
        status VARCHAR(20),
        FOREIGN KEY (patient_id) REFERENCES patient_records(patient_id)
    );
    """)

    # Import, preprocess, and insert data
    patient_data, hospital_data, public_health_data, appointments_data = import_data()
    patient_data, hospital_data, public_health_data, appointments_data = preprocess_data(patient_data, hospital_data, public_health_data, appointments_data)
    insert_data(conn, patient_data, hospital_data, public_health_data, appointments_data)
    conn.close()

if __name__ == "__main__":
    setup_database()  # Insert initial data
    while True:
        menu.show_menu()
