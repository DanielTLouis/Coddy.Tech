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
    elif(choice == 5):
        loop = False 
    else:
        print("Please enter a valid input: a number 1-5")
print("Exiting the Daily Expense Tracker. Goodbye!")
