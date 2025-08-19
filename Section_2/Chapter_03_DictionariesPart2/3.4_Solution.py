def print_employee_details(employee_data):
    # Write code here
  if not employee_data:
    print("No data available")
  for key, value in employee_data.items():
    print(key + ": " + tr(value))
