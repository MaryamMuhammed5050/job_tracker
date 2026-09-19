from tracker import (
    load_applications,
    add_application,
    view_applications,
    update_application,
    delete_application,
    search_applications
)


def show_menu():
    print("\n--- Job Application Tracker ---")
    print("1. Add application")
    print("2. View applications")
    print("3. Update application")
    print("4. Delete application")
    print("5. Search applications")
    print("6. Exit")


applications = load_applications()


while True:
    show_menu()

    choice = input("Choose an option: ")

    if choice == "1":
        print("\n--- Add Application ---")

        company = input("Enter company name: ")
        job_title = input("Enter job title: ")
        status = input("Enter application status: ")

        add_application(applications, company, job_title, status)

        print("Application added successfully.")

    elif choice == "2":
        view_applications(applications)

    elif choice == "3":
        update_application(applications)

    elif choice == "4":
        delete_application(applications)

    elif choice == "5":
        search_applications(applications)

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")