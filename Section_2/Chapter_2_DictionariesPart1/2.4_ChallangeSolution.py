def update_inventroy(inventory_dict, item, quantity):
  if(item in inventory_dict):
    inventory_dict[item]+=quantity
  else:
    inventory_dict[item]=quantity
  return inventory_dict
