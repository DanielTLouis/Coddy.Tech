inventory = dict()

def check_availability(item):
    try: 
        if(item not in inventory):
            return "Item not found"
        else:
            return inventory[item]["stock"]
    except Exception as e:
        print("Failed to execute")

def update_stock(item, quantity):
    try:
        if(item not in inventory):
            raise Exception("Not Found")
        elif(inventory[item]["stock"] + quantity < 0):
            raise Exception("Negative")
        inventory[item]["stock"] += quantity
        print(f"Stock for '{item}' updated successfully.")     
    except Exception as e:
        if(str(e) == "Not Found"):
            print(f"Error: Item '{item}' not found.")
        elif(str(e) == "Negative"):
            print(f"Error: Insufficient stock for '{item}'.")

def add_item(item, price, stock):
    try:
        if(item in inventory):
            raise Exception("exists")
        temp_dict = dict()
        temp_dict["price"] = price
        temp_dict["stock"] = stock
        inventory[item] = temp_dict
        print(f"Item '{item}' added successfully.")
    except Exception as e:
        if(str(e) == "exists"):
            print(f"Error: Item '{item}' already exists.")

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"   
