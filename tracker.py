import json

FILE_NAME = "jobs.json"


def load_applications():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_applications(applications):
    with open(FILE_NAME, "w") as file:
        json.dump(applications, file, indent=4)


def add_application(applications, company, job_title, status):
    application = {
        "company": company,
        "job_title": job_title,
        "status": status
    }

    applications.append(application)
    save_applications(applications)


def view_applications(applications):
    if len(applications) == 0:
        print("\nNo applications found.")
        return

    print("\n--- Your Applications ---")

    for number, application in enumerate(applications, start=1):
        print(f"\nApplication {number}")
        print(f"Company: {application['company']}")
        print(f"Job title: {application['job_title']}")
        print(f"Status: {application['status']}")


def update_application(applications):
    if len(applications) == 0:
        print("\nNo applications found.")
        return

    view_applications(applications)

    try:
        number = int(input("\nEnter application number to update: "))

        if number < 1 or number > len(applications):
            print("Invalid application number.")
            return

        new_status = input("Enter new status: ")

        applications[number - 1]["status"] = new_status
        save_applications(applications)

        print("Application updated successfully.")

    except ValueError:
        print("Please enter a number.")


def delete_application(applications):
    if len(applications) == 0:
        print("\nNo applications found.")
        return

    view_applications(applications)

    try:
        number = int(input("\nEnter application number to delete: "))

        if number < 1 or number > len(applications):
            print("Invalid application number.")
            return

        deleted = applications.pop(number - 1)
        save_applications(applications)

        print(f"{deleted['company']} application deleted.")

    except ValueError:
        print("Please enter a number.")


def search_applications(applications):
    if len(applications) == 0:
        print("\nNo applications found.")
        return

    search = input("\nEnter company name or job title: ").lower()

    found = False

    for application in applications:
        company = application["company"].lower()
        job_title = application["job_title"].lower()

        if search in company or search in job_title:
            print("\n--- Application Found ---")
            print(f"Company: {application['company']}")
            print(f"Job title: {application['job_title']}")
            print(f"Status: {application['status']}")
            found = True

    if not found:
        print("No matching application found.")