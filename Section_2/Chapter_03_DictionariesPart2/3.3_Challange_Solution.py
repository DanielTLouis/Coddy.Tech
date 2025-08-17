def check_inventory(inventory, item):
    # Write code here
  if item not in inventroy:
    print(item + " is not in stock.")
    return
  else:
    print(item + " is in stock. Quantity: " + str(inventroy[item])) 
    return 
