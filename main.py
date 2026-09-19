from tracker import add_application, view_applications


def show_menu():
    print("\n--- Job Application Tracker ---")
    print("1. Add application")
    print("2. View applications")
    print("3. Exit")


while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        print("\n--- Add Application ---")

        company = input("Enter company name: ")
        job_title = input("Enter job title: ")
        status = input("Enter application status: ")

        add_application(company, job_title, status)

        print("Application added successfully.")

    elif choice == "2":
        view_applications()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")