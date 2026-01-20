def process_data(input_string):
    try:
        # Try to convert the input string to an integer
        num = int(input_string)
        # Calculate 100 divided by the input value
        result = 100 / num        
        # Return the result
        return result 
    except ValueError:
        # Handle the case where input cannot be converted to an integer
        print("Input must be a number!")
    except ZeroDivisionError:
        # Handle the case where input is zero
        print("Cannot divide by zero!")
    except:
        # Handle any other unexpected exceptions
        print("An unexpected error occurred!")
    return None
