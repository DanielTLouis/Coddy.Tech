def filter_and_square_set(input_set):
    # Write code here
    new_set=set()
    for i in input_set:
        if i % 2 != 0:
            new_set.add(i*i)
    return new_set
