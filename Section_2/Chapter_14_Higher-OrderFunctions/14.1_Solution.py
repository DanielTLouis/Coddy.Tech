def convert_to_uppercase(strings):
    # Use map() with a lambda function to convert strings to uppercase
    uppercase_strings = map(lambda x: x.upper(), strings)
    
    # Return the list of uppercase strings
    return list(uppercase_strings)
