from db_config import create_connection

def view_patients():
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient_records")
    rows = cursor.fetchall()

    print("\n--- Patient Records ---")
    if rows:
        for row in rows:
            print(f"Patient ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Gender: {row[2]}")
            print(f"Diagnosis Date: {row[3]}")
            print(f"Medical History: {row[4]}")
            print(f"Visit Records: {row[5]}")
            print(f"Treatment Plan: {row[6]}")
            print(f"Outcome: {row[7]}")
            print(f"Date of Birth: {row[8]}")
            print(f"Contact Info: {row[9]}")
            print(f"Insurance Info: {row[10]}")
            print(f"Ethnicity: {row[11]}")
            print(f"Allergies: {row[12]}")
            print("\n---------------------------")
    else:
        print("No patient records found.")
    print("\n")

    conn.close()

def view_hospital_data():
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM hospital_data")
    rows = cursor.fetchall()

    print("\n--- Hospital Data ---")
    if rows:
        for row in rows:
            print(f"Record ID: {row[0]}")
            print(f"Department: {row[1]}")
            print(f"Bed Availability: {row[2]}")
            print(f"Doctors Available: {row[3]}")
            print(f"Equipment Status: {row[4]}")
            print(f"Staff Schedule: {row[5]}")
            print(f"Resource Utilization: {row[6]}")
            print("\n---------------------------")
    else:
        print("No hospital data found.")
    print("\n")

    conn.close()

def view_public_health_data():
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public_health_data")
    rows = cursor.fetchall()

    print("\n--- Public Health Data ---")
    if rows:
        for row in rows:
            print(f"Record ID: {row[0]}")
            print(f"Disease: {row[1]}")
            print(f"Geographic Region: {row[2]}")
            print(f"Health Trend: {row[3]}")
            print(f"Public Health Intervention: {row[4]}")
            print(f"Impact on Operations: {row[5]}")
            print(f"Vaccination Rate: {row[6]}")
            print(f"Healthcare Access: {row[7]}")
            print(f"Economic Impact: {row[8]}")
            print("\n---------------------------")
    else:
        print("No public health data found.")
    print("\n")

    conn.close()

def add_patient():
    name = input("Enter patient name: ")
    gender = input("Enter patient gender: ")
    diagnosis_date = input("Enter diagnosis date (YYYY-MM-DD): ")
    medical_history = input("Enter medical history: ")
    visit_records = input("Enter visit records: ")
    treatment_plan = input("Enter treatment plan: ")
    outcome = input("Enter outcome: ")
    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
    contact_info = input("Enter contact info: ")
    insurance_info = input("Enter insurance info: ")
    ethnicity = input("Enter ethnicity: ")
    allergies = input("Enter allergies: ")

    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    query = f"""
    INSERT INTO patient_records 
    (name, gender, diagnosis_date, medical_history, visit_records, treatment_plan, outcome, date_of_birth, contact_info, insurance_info, ethnicity, allergies) 
    VALUES 
    ('{name}', '{gender}', '{diagnosis_date}', '{medical_history}', '{visit_records}', '{treatment_plan}', '{outcome}', '{date_of_birth}', '{contact_info}', '{insurance_info}', '{ethnicity}', '{allergies}')
    """
    cursor.execute(query)
    conn.commit()

    print("\nPatient record added successfully.\n")

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

    print("\nHospital data added successfully.\n")

    conn.close()

def add_public_health_data():
    disease = input("Enter disease: ")
    geographic_region = input("Enter geographic region: ")
    health_trend = input("Enter health trend: ")
    public_health_intervention = input("Enter public health intervention: ")
    impact_on_operations = input("Enter impact on operations: ")
    vaccination_rate = input("Enter vaccination rate: ")
    healthcare_access = input("Enter healthcare access: ")
    economic_impact = input("Enter economic impact: ")

    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    query = f"""
    INSERT INTO public_health_data 
    (disease, geographic_region, health_trend, public_health_intervention, impact_on_operations, vaccination_rate, healthcare_access, economic_impact) 
    VALUES 
    ('{disease}', '{geographic_region}', '{health_trend}', '{public_health_intervention}', '{impact_on_operations}', '{vaccination_rate}', '{healthcare_access}', '{economic_impact}')
    """
    cursor.execute(query)
    conn.commit()

    print("\nPublic health data added successfully.\n")

    conn.close()

def find_patient_by_name():
    name = input("Enter patient name to search: ")

    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    query = f"SELECT * FROM patient_records WHERE name LIKE '%{name}%'"
    cursor.execute(query)
    rows = cursor.fetchall()

    print("\n--- Search Results ---")
    if rows:
        for row in rows:
            print(f"Patient ID: {row[0]}")
            print(f"Name: {row[1]}")
            print(f"Gender: {row[2]}")
            print(f"Diagnosis Date: {row[3]}")
            print(f"Medical History: {row[4]}")
            print(f"Visit Records: {row[5]}")
            print(f"Treatment Plan: {row[6]}")
            print(f"Outcome: {row[7]}")
            print(f"Date of Birth: {row[8]}")
            print(f"Contact Info: {row[9]}")
            print(f"Insurance Info: {row[10]}")
            print(f"Ethnicity: {row[11]}")
            print(f"Allergies: {row[12]}")
            print("\n---------------------------")
    else:
        print("No patients found with that name.")
    print("\n")

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

    print("\n--- Search Results ---")
    if rows:
        for row in rows:
            print(f"Record ID: {row[0]}")
            print(f"Department: {row[1]}")
            print(f"Bed Availability: {row[2]}")
            print(f"Doctors Available: {row[3]}")
            print(f"Equipment Status: {row[4]}")
            print(f"Staff Schedule: {row[5]}")
            print(f"Resource Utilization: {row[6]}")
            print("\n---------------------------")
    else:
        print("No hospital data found for that department.")
    print("\n")

    conn.close()

