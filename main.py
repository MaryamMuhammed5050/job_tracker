def show_menu():
    print("\n--- Job Application Tracker ---")
    print("1. Add application")
    print("2. view application")
    print("3. Exit")

while True:
    show_menu()
    choice = input("choose an option: ")

    if choice == "1":
        print("adding application (building in progress)")
    elif choice == "2":
        print("viewing application (building in progress)")
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid choice, try again.")