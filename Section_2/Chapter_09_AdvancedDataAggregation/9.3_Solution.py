# Starter inputs
numbers = [5, 3, 8, 1, 2]
words = ["elephant", "cat", "dolphin", "bee"]

# Task 1: Sort numbers in ascending order
ascending_numbers=sorted(numbers)
# Task 2: Sort numbers in descending order
descending_numbers=sorted(numbers, reverse=True)
# Task 3: Sort words alphabetically
alphabetical_words=sorted(words)
# Task 4: Sort words by length
length_sorted_words=sorted(words, key=len)
# Replace 'pass' with your code for each task


# Print the results
print("Ascending:", ascending_numbers)
print("Descending:", descending_numbers)
print("Alphabetical:", alphabetical_words)
print("By Length:", length_sorted_words)
