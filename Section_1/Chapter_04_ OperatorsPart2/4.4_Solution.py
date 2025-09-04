age = int(input())
has_license = input().lower() == "true"
has_insurance = input().lower() == "true"

result = age >= 18 and has_license and has_insuance # Complete this line to check if all conditions are met

print(result)
