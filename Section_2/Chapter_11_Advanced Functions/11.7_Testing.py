def sum_nested(nested_list):
    total = 0
    for i in nested_list:
        if(isinstance(i)):
            sum_nested(i)
        else:
            total += i
    return total 
