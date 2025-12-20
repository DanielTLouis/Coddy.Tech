temperatures = [72, 68, 75, 80, 65, 70, 78]
humidity = [60, 55, 65, 70, 50, 58, 62]

# TODO: Find the highest and lowest temperature from the 'temperatures' list using max() and min()
min_temp = min(temperatures)
max_temp = max(temperatures)
# TODO: Find the highest and lowest humidity from the 'humidity' list using max() and min()
min_hum = min(humidity)
max_hum = max(humidity)
# TODO: Print the highest temperature. Make sure to include the degree Fahrenheit symbol (°F).
# Example format: "Highest temperature: 80°F"
print(f"Highest temperature: {max_temp}°F")
# TODO: Print the lowest temperature. Use the same format.
# Example format: "Lowest temperature: 65°F"
print(f"Lowest temperature: {min_temp}°F")
# TODO: Print the highest humidity. Make sure to include the percentage symbol (%).
# Example format: "Highest humidity: 70%"
print(f"Highest humidity: {max_hum}%")
# TODO: Print the lowest humidity. Use the same format.
# Example format: "Lowest humidity: 50%"
print(f"Lowest humidity: {min_hum}%")
