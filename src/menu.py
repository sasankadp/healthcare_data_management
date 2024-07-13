import queries

def show_menu():
    print("1. View Patients")
    print("2. View Hospital Data")
    print("3. View Public Health Data")
    print("4. Add Patient")
    print("5. Add Hospital Data")
    print("6. Add Public Health Data")
    print("7. Find Patient by Name")
    print("8. Find Hospital by Department")
    print("9. View Appointments")
    print("10. Schedule Appointment")
    print("11. Cancel Appointment")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        queries.view_patients()
    elif choice == '2':
        queries.view_hospital_data()
    elif choice == '3':
        queries.view_public_health_data()
    elif choice == '4':
        queries.add_patient()
    elif choice == '5':
        queries.add_hospital_data()
    elif choice == '6':
        queries.add_public_health_data()
    elif choice == '7':
        queries.find_patient_by_name()
    elif choice == '8':
        queries.find_hospital_by_department()
    elif choice == '9':
        queries.view_appointments()
    elif choice == '10':
        queries.schedule_appointment()
    elif choice == '11':
        queries.cancel_appointment()
    elif choice == '12':
        exit()
    else:
        print("Invalid choice. Please try again.")
