def fizzbuzz(n):
    if n % 3 == 0 and n % 7 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 7 == 0:
        return "Buzz"
    for i in str(n):
      if i == '3':
        return "Almost Fizz"
    else:
        return f"{n}"
print("Welcome to FizzBuzz!")
num = int(input())
for i in range(1, num+1):
  result = fizzbuzz(i)
  print(result)
