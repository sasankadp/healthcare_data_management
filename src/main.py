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
    
    # Import, preprocess, and insert data
    patient_data, hospital_data, public_health_data = import_data()
    patient_data, hospital_data, public_health_data = preprocess_data(patient_data, hospital_data, public_health_data)
    insert_data(conn, patient_data, hospital_data, public_health_data)
    conn.close()

if __name__ == "__main__":
    setup_database()  # Insert initial data
    while True:
        menu.show_menu()
