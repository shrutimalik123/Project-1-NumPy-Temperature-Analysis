import numpy as np

# Sample data: Daily max temperatures (in Celsius) for 10 days
celsius_temps = np.array([25.5, 26.8, 23.0, 29.1, 28.5, 30.2, 27.9, 24.3, 22.0, 27.0])

print(f"Celsius Temperatures:\n{celsius_temps}")

# Convert to Fahrenheit
fahrenheit_temps = (celsius_temps * 9/5) + 32
print(f"\nFahrenheit Temperatures:\n{fahrenheit_temps}")
