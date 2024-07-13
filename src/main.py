import mysql.connector
from mysql.connector import Error
from db_config import create_connection
import menu
from data_import import import_data
from data_preprocessing import preprocess_data
from data_insertion import insert_data

def execute_sql_file(filename):
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()
    with open(filename, 'r') as sql_file:
        sql_commands = sql_file.read().split(';')

        for command in sql_commands:
            try:
                if command.strip() != '':
                    cursor.execute(command)
            except Error as e:
                print(f"The error '{e}' occurred while executing the command: {command}")

    conn.commit()
    conn.close()

def setup_database():
    # Connect to the specific database
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return

    # Import, preprocess, and insert data
    patient_data, hospital_data, public_health_data, appointments_data = import_data()
    patient_data, hospital_data, public_health_data, appointments_data = preprocess_data(patient_data, hospital_data, public_health_data, appointments_data)
    insert_data(conn, patient_data, hospital_data, public_health_data, appointments_data)
    conn.close()

if __name__ == "__main__":
    setup_database()  # Set up database and insert initial data
    while True:
        menu.show_menu()
