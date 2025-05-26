original_list = input().split(',')
# Write your code below
list1 = original_list[2::4]
lsit2 = original_list[2:len(original_list)-2]
list3 = original_list[::-2]
list4 = original_list[-3:]
# Don't change below this line
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
print("List 4:", list4)
