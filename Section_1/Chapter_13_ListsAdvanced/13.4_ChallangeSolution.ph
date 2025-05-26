numbers = input().split()
# Write your code below
new_numbers = numbers + numbers[::-1]
new_numbers = numbers[0:1] + new_numbers + numbers[-1:]
new_numebrs = new_numbers + new_numbers 
print(new_numebrs)
