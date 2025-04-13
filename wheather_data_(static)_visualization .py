import matplotlib.pyplot as plt

# Sample weather data for a week
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [30, 32, 33, 31, 29, 35, 36]  # in Celsius
humidity = [40, 45, 50, 42, 38, 55, 60]     # in %
weather_conditions = ['Sunny', 'Rainy', 'Sunny', 'Cloudy', 'Sunny', 'Sunny', 'Rainy']

# Count weather condition occurrences for pie chart
from collections import Counter
weather_count = Counter(weather_conditions)

# 1. Line Plot for Temperature
plt.figure(figsize=(8,5))
plt.plot(days, temperature, marker='o', color='orange')
plt.title('Temperature Over a Week')
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Bar Chart for Humidity
plt.figure(figsize=(8,5))
plt.bar(days, humidity, color='skyblue')
plt.title('Humidity Over a Week')
plt.xlabel('Days')
plt.ylabel('Humidity (%)')
plt.tight_layout()
plt.show()

# 3. Pie Chart for Weather Conditions
plt.figure(figsize=(6,6))
plt.pie(weather_count.values(), labels=weather_count.keys(), autopct='%1.1f%%', startangle=140, colors=['gold', 'gray', 'lightgreen'])
plt.title('Weather Condition Distribution')
plt.tight_layout()
plt.show()
