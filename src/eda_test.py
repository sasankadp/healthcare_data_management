# eda_test.py
from data_import import import_data
from data_preprocessing import preprocess_data
from eda import visualize_data

def main():
    # Import data
    patient_data, hospital_data, public_health_data = import_data()
    
    # Preprocess data
    patient_data, hospital_data, public_health_data = preprocess_data(patient_data, hospital_data, public_health_data)
    
    # Visualize data
    visualize_data(patient_data, hospital_data, public_health_data)

if __name__ == "__main__":
    main()
