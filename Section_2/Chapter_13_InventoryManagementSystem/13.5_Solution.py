inventory = dict()

def sales_report(sales):
    total = 0
    for key, value in sales.items():
        try:
            if key in inventory:
                if(inventory[key]["stock"] < value):
                    raise Exception("Insufficient")
                else:
                    inventory[key]["stock"] -= value
                    total += inventory[key]["price"] * value
            else:
                raise Exception("Not Found")
        except Exception as e:
            if(str(e) == "Not Found"):
                print(f"Error: Item '{key}' not found.")
            elif(str(e) == "Insufficient"):
                print(f"Error: Insufficient stock for '{key}'.")
    return f"Total revenue: ${total:.2f}" 
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

add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)   
