group1 = eval(input())
group2 = eval(input())
group3 = eval(input())

# Write your code below
intersection_result = group1 & group2 & group3
difference_result = group1 - group2 - group3 

# Print the results
print("Members in all groups:", sorted(list(intersection_result)))
print("Unique members in group1:", sorted(list(difference_result)))
