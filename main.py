import json as js
import csv


def banner():
    banner = """
███████╗██╗  ██╗██████╗ ███████╗███╗   ██╗███████╗███████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝████╗  ██║██╔════╝██╔════╝
█████╗   ╚███╔╝ ██████╔╝█████╗  ██╔██╗ ██║███████╗█████╗
██╔══╝   ██╔██╗ ██╔═══╝ ██╔══╝  ██║╚██╗██║╚════██║██╔══╝
███████╗██╔╝ ██╗██║     ███████╗██║ ╚████║███████║███████╗
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝
            EXPENSE TRACKER
1. Expense Entry
2. Convert To CSV
3. Exit
"""
    print(banner)


def load_data():
    try:
        with open("data.json", "r") as f:
            data = js.load(f)
    except (FileNotFoundError, js.JSONDecodeError):
        data = []
    return data


def save_to_json(new_expenses):
    data = load_data()
    data.extend(new_expenses)
    with open("data.json", "w") as f:
        js.dump(data, f, indent=4)
    print("Expenses saved successfully.")


def convert_to_csv():
    data = load_data()
    if not data:
        print("No data found.")
        return

    with open("expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "amount", "category"])
        writer.writeheader()
        writer.writerows(data)

    print("CSV file created as expenses.csv")


def expense_entry():
    print(
        """
==============
Enter Expenses
=============="""
    )

    no_of_expenses = int(input("Enter the number of expenses you want to add: "))
    expenses = []

    for i in range(1, no_of_expenses + 1):
        expense_name = input(f"Enter name of expense {i}: ")

        while True:
            try:
                spent_amount = float(
                    input(f"Enter the amount you spent on {expense_name}: ")
                )
                break
            except ValueError:
                print("Value expected in decimal.")

        desc = input("Enter the Category of the Expense: ")

        expenses.append(
            {
                "name": expense_name,
                "amount": spent_amount,
                "category": desc,
            }
        )

    return expenses


def main_menu():
    while True:
        banner()

        try:
            usr_input = int(input("Select An Option: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if usr_input == 1:
            new_expenses = expense_entry()
            save_to_json(new_expenses)

        elif usr_input == 2:
            convert_to_csv()

        elif usr_input == 3:
            print("Exiting.")
            break

        else:
            print("Invalid option. Try again.")


main_menu()

# View my github https://github.com/jatharkartik01-png/jatharkartik01-png
