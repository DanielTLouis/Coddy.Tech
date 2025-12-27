def dictionary_sorter(data_dict):
    # Write code here
    temp_dict=dict()
    sorted_dict=dict()
    for i in data_dict:
        temp_dict[data_dict[i]] = i
    sorted(temp_dict) 
    for i in temp_dict:
        sorted_dict[temp_dict[i]] = i
    return sorted_dict
