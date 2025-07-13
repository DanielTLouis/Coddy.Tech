def calculate_discount(price, discount_percentage):
  # Write code here
  price = price - (0.01 * float(discount_percentage) * price)
  price = round(price, 2)
  return price
