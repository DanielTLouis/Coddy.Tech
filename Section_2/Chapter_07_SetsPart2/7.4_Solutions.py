def check_sets(set1, set2):
    # Check if set1 is a subset of set2
    is_subset = set1 <= set2

    # Check if set2 is a superset of set1
    is_superset = set2 >= set1

    # Check if set1 is a proper subset of set2
    is_proper_subset = set1 < set2

    # Check if set2 is a proper superset of set1
    is_proper_superset = set2 > set1

    # Return a dictionary containing the results
    return {
        "is_subset": is_subset,
        "is_superset": is_superset,
        "is_proper_subset": is_proper_subset,
        "is_proper_superset": is_proper_superset
    }
