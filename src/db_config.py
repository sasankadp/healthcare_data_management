import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=1234,
            user="root",
            password="1qa2ws3ed",
            database="healthcare_data"
        )
        if connection.is_connected():
            print("\nImSasa Health Care Mangement System") # Connection to MySQL DB successful
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
