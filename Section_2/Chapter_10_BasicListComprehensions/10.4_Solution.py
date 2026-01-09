def sum_positive_evens(numbers):
    # Write code here
    sums=sum(n for n in numbers if n > 0 and n % 2 == 0)
    return sums
