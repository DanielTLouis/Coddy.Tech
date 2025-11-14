def set_operations(set1, set2):
    # Calculate the union
    union_result = set1 | set2 

    # Calculate the intersection
    intersection_result = set1 & set2

    # Calculate the difference
    difference_result = set1 - set2

    # Calculate the symmetric difference
    symmetric_difference_result = set1 ^ set2

    # Return a dictionary containing the results
    return {
        "union": union_result,
        "intersection": intersection_result,
        "difference": difference_result,
        "symmetric_difference": symmetric_difference_result
    }
