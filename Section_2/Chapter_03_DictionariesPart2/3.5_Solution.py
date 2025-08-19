def frequency_counter(data_list):
  # Write code here
  for var in data_list:
    if not var in dic:
      dic[var] = 1
    else:
      dic[var] += 1
  return dic
