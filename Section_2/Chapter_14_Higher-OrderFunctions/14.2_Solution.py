def get_long_strings(strings):
    # Use filter() with a lambda function to select strings with length greater than 5
    long_strings = filter(lambda x : len(x) > 5, strings)
    
    # Return the list of selected strings
    return list(long_strings)
