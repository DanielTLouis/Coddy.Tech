lst = input().split(",")
# Write your code below
if len(lst) % 2 == 0:
    print(lst[len(lst)//2 -1: len(lst)//2 + 1])
else:
    print(lst[len(lst)//2 -1: len(lst)//2 + 2])
