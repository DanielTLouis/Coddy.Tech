def compare_strings(str1, str2):
    # Write code here
    dic = {}
    dic['is_substring'] =  str1 in str2 
    dic['starts_with'] = str2.startswith(str1)
    dic['ends_with'] = str2.endswith(str1)
    dic['is_equal'] = str1.lower() == str2.lower()
    return dic
