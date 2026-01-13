input_list = input().split(', ')
# Write your code below
if len(input_list) >= 5:
  new_lst = input_list[0:2] + input_list[-2:]
  print(new_lst)
else:
  new_lst = [input_list[0] , input_list[len(input_list)-1]] 
  print(new_lst) 
