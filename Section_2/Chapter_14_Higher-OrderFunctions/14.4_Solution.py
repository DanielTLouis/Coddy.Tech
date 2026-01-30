def pos_num_fun(x):
    if(x % 2 == 0):
        return x * 2
    else:
        return x * 3
def process_numbers(numbers):
    # Write your code below
    processed_numbers = map(lambda x : pos_num_fun(x), filter(lambda x : x > 0, numbers))
    
    return list(processed_numbers)
