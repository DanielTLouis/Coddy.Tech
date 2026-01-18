def sum_digits(n):
    # Write code here
    if(n < 10):
        return n 
    return (n%10) + sum_digits((n // 10))
