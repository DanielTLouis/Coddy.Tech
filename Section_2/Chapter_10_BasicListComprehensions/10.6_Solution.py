def elements_of_freedom(elements):
    # Your solution here
    new_list = []
    # Step 1: Filter elements with length >= 5
    new_list = [n for n in elements if len(n) >= 5]
    # Step 2: Convert filtered elements to uppercase
    new_list = [n.upper() for n in new_list]
    # Step 3: Create a list of unique elements
    new_list2= []
    for n in new_list:
        if n not in new_list2:
            new_list2.append(n) 
    # Step 4: Return the final result
    return new_list2
    pass
