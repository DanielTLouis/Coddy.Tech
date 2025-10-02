temperature = int(input()) # Don't change this line
weather = "unset"
# Type your code below
if temperature < 0:
    weather = "Freezing" 
elif temperature < 16: 
    weather = "Cold" 
elif temperature < 25:
    weather = "Mild" 
else :
    weather = "Hot" 

# Don't change the line below
print(f"weather = {weather}")
