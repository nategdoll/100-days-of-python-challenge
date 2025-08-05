import json

while True:
    print("Welcome to the Birthday Manager!")
    print("1. Add a new birthday")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "2":
        print("Exiting the Birthday Manager.")
        break
    elif choice != "1":
        print("Invalid choice, please try again.")
        continue
    else:
        name = input("Enter name: ").strip()
        birthday = input("Enter birthday (YYYY-MM-DD): ").strip()
        email = input("Enter email: ").strip()

        # Load existing birthdays
        try:
            with open("birthdays.json", "r") as file:
                birthdays_data = json.load(file)
        except FileNotFoundError:
            birthdays_data = {"birthdays": []}

        # Add new birthday
        birthdays_data["birthdays"].append({
            "name": name,
            "birthday": birthday,
            "email": email
        })

        # Save updated birthdays
        with open("birthdays.json", "w") as file:
            json.dump(birthdays_data, file, indent=4)

        print(f"Birthday for {name} added successfully!")