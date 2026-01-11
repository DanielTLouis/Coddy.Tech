def house_of_lists(list_of_lists):
    # Write code here
    new_list = []
    for i in list_of_lists:
        if(sum(i) < 50):
            new_list.append(i)
    new_list = [n for inner in new_list for n in inner if n < 5]
    return new_list
