expenses = []


def add_expense():
    description = input("Description: ")
    amount = float(input("Amount: "))
    expenses.append({"description": description, "amount": amount})
    print("Expense added.")


def show_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - {expense['amount']:.2f}")


def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total expenses: {total:.2f}")


def show_average():
    if not expenses:
        print("No expenses recorded.")
        return
    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)
    print(f"Average expense: {average:.2f}")


def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add an expense")
        print("2. Show expenses")
        print("3. Show total")
        print("4. Exit")
        print("5. Show average")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        elif choice == "5":
            show_average()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()