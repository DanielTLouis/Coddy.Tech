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
    if(choice == 5):
        loop = False 
print("Exiting the Daily Expense Tracker. Goodbye!")
