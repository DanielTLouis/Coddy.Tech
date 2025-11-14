def remove_duplicates(numbers):
    # Write code here
    numbers_to_set=set()
    for i in numbers:
        numbers_to_set.add(i)
    return list(numbers_to_set)
