def fizzbuzz(n):
    if n % 3 == 0 and n % 7 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 7 == 0:
        return "Buzz"
    else:
        return f"{n}"
print("Welcome to FizzBuzz!")
num = int(input())
result = fizzbuzz(num)
print(result)
