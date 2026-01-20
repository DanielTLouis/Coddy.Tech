def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    dic = dict()
    # Process each order in the list
    for order in orders:
        try:
            # Split the order and add to cart
            order_split = order.split(':')
            if(int(order_split[1]) < 0):
                raise Exception("Negative")
            if(order_split[0] in dic):
                dic[order_split[0]] += int(order_split[1])
            else:
                dic[order_split[0]]=int(order_split[1])
        # Handle potential errors 
        except ValueError:
            # Handle value errors
            print(f"Invalid quantity: {order}")
        except Exception as e:
            if(str(e) == "Negative"):
                print(f"Negative quantity not allowed: {order}")
            else:
                # Handle unexpected errors
                print(f"Invalid format: {order}")
    # Return the completed cart
    return dic
