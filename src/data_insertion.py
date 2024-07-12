from db_config import create_connection
from mysql.connector import Error

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        #print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_data(connection, patient_data, hospital_data, public_health_data):
    patient_queries = [
        f"INSERT INTO patient_records (name, age, gender, diagnosis_date, medical_history, visit_records, treatment_plan, outcome) VALUES ('{record['name']}', {record['age']}, '{record['gender']}', '{record['diagnosis_date']}', '{record['medical_history']}', '{record['visit_records']}', '{record['treatment_plan']}', '{record['outcome']}')"
        for record in patient_data
    ]
    hospital_queries = [
        f"INSERT INTO hospital_data (department, bed_availability, doctors_available, equipment_status, staff_schedule, resource_utilization) VALUES ('{record['department']}', {record['bed_availability']}, {record['doctors_available']}, '{record['equipment_status']}', '{record['staff_schedule']}', '{record['resource_utilization']}')"
        for record in hospital_data
    ]
    public_health_queries = [
        f"INSERT INTO public_health_data (disease, geographic_region, health_trend, public_health_intervention, impact_on_operations) VALUES ('{record['disease']}', '{record['geographic_region']}', '{record['health_trend']}', '{record['public_health_intervention']}', '{record['impact_on_operations']}')"
        for record in public_health_data
    ]
    
    for query in patient_queries:
        execute_query(connection, query)
    for query in hospital_queries:
        execute_query(connection, query)
    for query in public_health_queries:
        execute_query(connection, query)
