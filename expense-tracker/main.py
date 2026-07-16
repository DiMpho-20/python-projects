from tracker import ExpenseTracker


def main():

    expense = ExpenseTracker()

    while True:
        print ("\n---------Expenses-----------")
        print ("1. Add Expense." )
        print("2. View all Expenses")
        print ("3. Delete expense")
        print ("4. Monthly report.")
        print("5. Total spent.")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Add expense")
            try:
                amount=float(input("Amount: "))
            except ValueError:
                print("Please Enter a valid number.")
                continue
            category=input("Category: ")
            description = input("Description: ")
            expense.add_expense(amount,category,description)

        elif choice== '2':
            print( "All of my expenses")
            expense.view_all()
        
        elif choice == "3":
            try:
                id = int(input("Expense id: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue

            expense.delete_expense(id)
            print(f'Deleted expense : {id}')
        elif choice == "4":
            try:
                month = int(input("Enter month (1-12): "))

                if not 1 <= month <= 12:
                    print("Month must be between 1 and 12.")
                    continue

                expense.monthly_report(month)

            except ValueError:
                print("Please enter a valid month number.")
                

        elif choice== '5':
            print( "Total spent ")
            expense.total_spent()

        elif choice =='6':
            print("Goodbye thanks!!")
            break

if  __name__ == "__main__":
    main()
