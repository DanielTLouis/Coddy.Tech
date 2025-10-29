# Given data
names = ["Alice", "Bob", "Charlie"]
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

# Write code here
print("Alice is in the list.") if "Alice" in names else print("Alice is in the list.")
print("David is in the list.") if "David" in names else print("David is not in the list.")
print("Bob is in the dictionary.") if "Bob" in grades else print("Bob is in the dictionary.")
print("Eve is in the dictionary.") if "Eve" in grades else print("Eve is not in the dictionary.")
