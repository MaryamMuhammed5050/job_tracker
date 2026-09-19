applications = []


def add_application(company, job_title, status):
    application = {
        "company": company,
        "job_title": job_title,
        "status": status
    }

    applications.append(application)


def view_applications():
    if len(applications) == 0:
        print("\nNo applications yet.")
        return

    print("\n--- Job Applications ---")

    for application in applications:
        print(f"Company: {application['company']}")
        print(f"Job title: {application['job_title']}")
        print(f"Status: {application['status']}")
        print()