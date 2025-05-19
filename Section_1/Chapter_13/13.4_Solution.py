lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below
new_lst = []
for i in lst1: 
    if i not in lst2:
        new_lst.append(i)
print(new_lst)
