def iterate_and_filter_set(input_set):
    # Write code here
    new_set = set()
    for i in input_set:
        if i <= 10:
            new_set.add(i)
    return new_set
