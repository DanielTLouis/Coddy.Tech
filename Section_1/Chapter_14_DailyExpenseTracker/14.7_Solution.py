print("Welcome to the Daily Expense Tracker!")
print("")
print("Menu:") 
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
loop = True
expenses = []
while loop:
    choice = int(input()) 
    if(choice == 1):
        expenses.append(float(input()))
        print("Expense added successfully!")
    elif(choice == 2):
        if(not expenses):
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i+1}. {expenses[i]}")
    elif(choice == 3):
        if(not expenses):
            print("No expenses recorded yet.")
        else:
            total = 0
            for i in expenses:
                total += i
            print(f"Total expense: {total}")
            print(f"Average expense: {total / len(expenses)}")
    elif(choice == 4):
        expenses = []
        print("All expenses cleared.")
    elif(choice == 5):
        loop = False 
    else:
        print("Invalid choice. Please try again.")
print("Exiting the Daily Expense Tracker. Goodbye!")
