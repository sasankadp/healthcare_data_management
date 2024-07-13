import json

def import_data():
    # Reading data from JSON files
    with open('data/patient_data.json') as f:
        patient_data = json.load(f)
    
    with open('data/hospital_data.json') as f:
        hospital_data = json.load(f)
    
    with open('data/public_health_data.json') as f:
        public_health_data = json.load(f)

    with open('data/appointments_data.json') as f:
        appointments_data = json.load(f)
    
    return patient_data, hospital_data, public_health_data, appointments_data
