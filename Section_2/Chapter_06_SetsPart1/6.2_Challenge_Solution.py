def manage_list(list1, element_to_append, index_to_remove):
    # Write code here
    list1.append(element_to_append)
    if(index_to_remove in list1):
        list1.remove(index_to_remove)
    if(len(list1) > 3):
        print("The list has more than 3 elements")
    else:
        print("The list has 3 or fewer elements")
