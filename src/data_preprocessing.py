import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(patient_data, hospital_data, public_health_data):
    # Convert JSON data to DataFrame
    patient_df = pd.DataFrame(patient_data)
    hospital_df = pd.DataFrame(hospital_data)
    public_health_df = pd.DataFrame(public_health_data)

    # Handle missing values
    patient_df.fillna({
        'gender': 'Unknown',
        'diagnosis_date': '1900-01-01',
        'medical_history': '',
        'visit_records': '',
        'treatment_plan': '',
        'outcome': 'Unknown',
        'date_of_birth': '1900-01-01',
        'contact_info': 'Unknown',
        'insurance_info': 'Unknown',
        'ethnicity': 'Unknown',
        'allergies': 'None'
    }, inplace=True)
    hospital_df.fillna('', inplace=True)
    public_health_df.fillna('', inplace=True)

    # Remove duplicates
    patient_df.drop_duplicates(inplace=True)
    hospital_df.drop_duplicates(inplace=True)
    public_health_df.drop_duplicates(inplace=True)

    # Resolve inconsistencies
    patient_df['diagnosis_date'] = pd.to_datetime(patient_df['diagnosis_date'])
    patient_df['date_of_birth'] = pd.to_datetime(patient_df['date_of_birth'])

    # Feature engineering: calculate patient age
    current_date = pd.to_datetime('today')
    patient_df['age'] = (current_date - patient_df['date_of_birth']).dt.days // 365

    # Normalization and scaling
    scaler = StandardScaler()
    patient_df[['age']] = scaler.fit_transform(patient_df[['age']])

    return patient_df.to_dict('records'), hospital_df.to_dict('records'), public_health_df.to_dict('records')
