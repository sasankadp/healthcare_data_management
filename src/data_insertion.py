from db_config import create_connection
from mysql.connector import Error

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_data(connection, patient_data, hospital_data, public_health_data, appointments_data):
    patient_queries = [
        f"INSERT INTO patient_records (name, gender, diagnosis_date, medical_history, visit_records, treatment_plan, outcome, date_of_birth, contact_info, insurance_info, ethnicity, allergies) VALUES ('{record['name']}', '{record['gender']}', '{record['diagnosis_date']}', '{record['medical_history']}', '{record['visit_records']}', '{record['treatment_plan']}', '{record['outcome']}', '{record['date_of_birth']}', '{record['contact_info']}', '{record['insurance_info']}', '{record['ethnicity']}', '{record['allergies']}')"
        for record in patient_data
    ]
    hospital_queries = [
        f"INSERT INTO hospital_data (department, bed_availability, doctors_available, equipment_status, staff_schedule, resource_utilization) VALUES ('{record['department']}', {record['bed_availability']}, {record['doctors_available']}, '{record['equipment_status']}', '{record['staff_schedule']}', '{record['resource_utilization']}')"
        for record in hospital_data
    ]
    public_health_queries = [
        f"INSERT INTO public_health_data (disease, geographic_region, health_trend, public_health_intervention, impact_on_operations, vaccination_rate, healthcare_access, economic_impact) VALUES ('{record['disease']}', '{record['geographic_region']}', '{record['health_trend']}', '{record['public_health_intervention']}', '{record['impact_on_operations']}', {record['vaccination_rate']}, '{record['healthcare_access']}', '{record['economic_impact']}')"
        for record in public_health_data
    ]
    appointments_queries = [
        f"INSERT INTO appointments (patient_id, doctor_name, appointment_date, status) VALUES ({record['patient_id']}, '{record['doctor_name']}', '{record['appointment_date']}', '{record['status']}')"
        for record in appointments_data
    ]

    for query in patient_queries:
        execute_query(connection, query)
    for query in hospital_queries:
        execute_query(connection, query)
    for query in public_health_queries:
        execute_query(connection, query)
    for query in appointments_queries:
        execute_query(connection, query)

def insert_appointment(connection, patient_id, doctor_name, appointment_date, status):
    query = f"""
    INSERT INTO appointments (patient_id, doctor_name, appointment_date, status)
    VALUES ({patient_id}, '{doctor_name}', '{appointment_date}', '{status}')
    """
    execute_query(connection, query)
