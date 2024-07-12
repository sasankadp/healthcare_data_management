from db_config import create_connection

def view_patients():
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient_records")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def view_hospital_data():
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hospital_data")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def view_public_health_data():
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public_health_data")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def add_patient():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    gender = input("Enter patient's gender: ")
    diagnosis_date = input("Enter diagnosis date (YYYY-MM-DD): ")
    medical_history = input("Enter medical history: ")
    visit_records = input("Enter visit records: ")
    treatment_plan = input("Enter treatment plan: ")
    outcome = input("Enter outcome: ")

    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    query = f"""
    INSERT INTO patient_records 
    (name, age, gender, diagnosis_date, medical_history, visit_records, treatment_plan, outcome) 
    VALUES 
    ('{name}', {age}, '{gender}', '{diagnosis_date}', '{medical_history}', '{visit_records}', '{treatment_plan}', '{outcome}')
    """
    cursor.execute(query)
    conn.commit()

    print("Patient record added successfully.")
    conn.close()

def add_hospital_data():
    department = input("Enter department: ")
    bed_availability = input("Enter bed availability: ")
    doctors_available = input("Enter number of doctors available: ")
    equipment_status = input("Enter equipment status: ")
    staff_schedule = input("Enter staff schedule: ")
    resource_utilization = input("Enter resource utilization: ")

    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    query = f"""
    INSERT INTO hospital_data 
    (department, bed_availability, doctors_available, equipment_status, staff_schedule, resource_utilization) 
    VALUES 
    ('{department}', {bed_availability}, {doctors_available}, '{equipment_status}', '{staff_schedule}', '{resource_utilization}')
    """
    cursor.execute(query)
    conn.commit()

    print("Hospital data added successfully.")
    conn.close()

def add_public_health_data():
    disease = input("Enter disease: ")
    geographic_region = input("Enter geographic region: ")
    health_trend = input("Enter health trend: ")
    public_health_intervention = input("Enter public health intervention: ")
    impact_on_operations = input("Enter impact on operations: ")

    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    query = f"""
    INSERT INTO public_health_data 
    (disease, geographic_region, health_trend, public_health_intervention, impact_on_operations) 
    VALUES 
    ('{disease}', '{geographic_region}', '{health_trend}', '{public_health_intervention}', '{impact_on_operations}')
    """
    cursor.execute(query)
    conn.commit()

    print("Public health data added successfully.")
    conn.close()

def find_patient_by_name():
    name = input("Enter patient's name to search: ")

    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    query = f"SELECT * FROM patient_records WHERE name LIKE '%{name}%'"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def find_hospital_by_department():
    department = input("Enter department to search: ")

    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    query = f"SELECT * FROM hospital_data WHERE department LIKE '%{department}%'"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def find_patients_by_diagnosis_date():
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    query = f"SELECT * FROM patient_records WHERE diagnosis_date BETWEEN '{start_date}' AND '{end_date}'"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()
