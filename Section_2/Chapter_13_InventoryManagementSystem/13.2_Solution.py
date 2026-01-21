inventory = dict()

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
add_item("Apple", 0.6, 30)  # Should print an error
print(inventory)  
