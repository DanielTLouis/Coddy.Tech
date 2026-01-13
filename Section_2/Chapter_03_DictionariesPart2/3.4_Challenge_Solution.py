def print_product_details(product_data):
    # Write code here
  if not product_data:
    print("No product information available")
  for key, value in public_data.items():
    print(key.capitalize() + ": " + str(value))
