import pandas as pd
from data_import import import_data
from data_preprocessing import preprocess_data

def preprocess_data_demo():
    # Import data using your data_import.py script
    patient_data, hospital_data, public_health_data = import_data()

    # Convert patient data to DataFrame for demonstration
    patient_df = pd.DataFrame(patient_data)

    # Print original data sample
    print("Original Patient Data Sample:")
    print(patient_df.head())

    # Feature engineering: calculate patient age from date_of_birth
    current_date = pd.to_datetime('today')
    patient_df['age'] = (current_date - pd.to_datetime(patient_df['date_of_birth'])).dt.days // 365

    # Preprocess the data using your data_preprocessing.py script
    preprocessed_patient_data, _, _ = preprocess_data(patient_df.to_dict('records'), hospital_data, public_health_data)

    # Convert preprocessed data back to DataFrame for consistency
    preprocessed_df = pd.DataFrame(preprocessed_patient_data)

    # Print preprocessed data sample
    print("Preprocessed Patient Data Sample:")
    print(preprocessed_df.head())

if __name__ == "__main__":
    preprocess_data_demo()
