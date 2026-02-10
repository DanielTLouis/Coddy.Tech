Recap - Simple Calculator


Challenge

Medium
Your Calculator class in calculator.py should:

Have a constructor that initializes a result attribute to 0
Include methods for add, subtract, multiply, and divide that each:
Take a number as an argument
Perform the operation between the current result and the number
Update the result attribute
Return the new result
Include a clear method that resets the result to 0
Include a get_result method that returns the current result
For the divide method, you must handle division by zero by:
Checking if the provided number equals 0
If it is zero, print exactly: "Error: Division by zero"
Leave the result attribute unchanged in this case
Return the unchanged result value
The driver.py file will import your Calculator class and test it with code similar to this:

from calculator import Calculator

calc = Calculator()
calc.add(5)       # result becomes 5
calc.multiply(3)  # result becomes 15
calc.subtract(2)  # result becomes 13
calc.divide(0)    # prints "Error: Division by zero", result remains 13
calc.divide(2)    # result becomes 6.5
calc.clear()      # result becomes 0
Follow the TODO comments in the calculator.py file to implement all required functionality.


