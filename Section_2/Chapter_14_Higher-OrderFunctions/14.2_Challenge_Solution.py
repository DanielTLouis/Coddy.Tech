def isPrime(num):
    if(num <= 1):
        return False
    elif(num == 2):
        return True
    elif(num % 2 == 0):
        return False
    else:
        for i in range(2,num):
                if (num % i == 0): 
                    return False
        return True

def get_prime_numbers(numbers):
    # Use filter() with a lambda function to select prime numbers
    prime_numbers = filter(lambda num : isPrime(num), numbers)
    
    # Return the list of selected prime numbers
    return list(prime_numbers)
