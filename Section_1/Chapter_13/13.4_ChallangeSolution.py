def not_mutual_friends(list1, list2):
    # Write your code below
    not_mutual_friends_lst = []
    for i in list1:
        if i not in list2:
            not_mutual_friends_lst.append(i)
    for i in list2: 
        if i not in list1:
            not_mutual_friends_lst.append(i)
    return not_mutual_friends_lst
