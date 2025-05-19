lst = input().split(",")
# Write your code below
lst1 = []
lst2 = []
lst3 = []

lst1 = lst[1::3]
lst2 = lst[5::-1]
lst3 = lst[len(lst)//2 : :2]
print(lst1)
print(lst2)
print(lst3)
