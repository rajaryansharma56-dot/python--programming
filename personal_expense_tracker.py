
expenses = []
amounts = []
categories = []

while True:

    print("\n====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Highest Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")

        expenses.append(name)
        amounts.append(amount)
        categories.append(category)

        print("Expense added successfully!")

    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses found!")

        else:
            print("\nYour Expenses:")

            for i in range(len(expenses)):
                print(expenses[i], "-", amounts[i], "-", categories[i])

    elif choice == "3":

        total = 0

        for i in range(len(amounts)):
            total = total + amounts[i]

        print("Total Expenses:", total)

    elif choice == "4":

        if len(amounts) == 0:
            print("No expenses found!")

        else:
            highest = amounts[0]

            for i in range(len(amounts)):

                if amounts[i] > highest:
                    highest = amounts[i]

            print("Highest Expense:", highest)

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")
