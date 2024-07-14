# predictive_test.py
from data_import import import_data
from data_preprocessing import preprocess_data
from predictive_modeling import train_predictive_model, predict_outcome

def main():
    # Import and preprocess data
    patient_data, hospital_data, public_health_data = import_data()
    patient_data, hospital_data, public_health_data = preprocess_data(patient_data, hospital_data, public_health_data)
    
    # Train predictive model
    model = train_predictive_model(patient_data)
    
    # Sample patient data for prediction
    sample_patient = {
        'age': 45,
        'gender': 'male',
        'medical_history': 'Hypertension, Diabetes',
        'visit_records': '2021-12-01, 2022-01-01',
        'treatment_plan': 'Medication, Diet',
        'outcome': 'Improved',
        'date_of_birth': '1977-01-01',
        'contact_info': '123456789',
        'insurance_info': 'XYZ Insurance',
        'ethnicity': 'Asian',
        'allergies': 'None'
    }

    # Predict outcome
    outcome = predict_outcome(model, sample_patient)
    print(f"Predicted Outcome: {outcome}")

if __name__ == "__main__":
    main()
