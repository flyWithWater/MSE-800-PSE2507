# Develop a Python project to perform the following tasks (import NumPy as np):
# Calculate and print the average temperature for the week using NumPy.
# Temperature data (in °C): [18.5, 19, 20, 25.0, 2, 30, 13.9]
# Determine and display the highest and lowest recorded temperatures.
# Convert all temperatures to Fahrenheit and print the converted values.
# (Use the formula: F = C × 9/5 + 32)
# Identify and print the indices of days where the temperature exceeded 20°C.


import numpy as np




tempOfAWeek = [18.5, 19, 20, 25.0, 2, 30, 13.9]

avgtemp = np.average(tempOfAWeek)
print(f"average temperature of the week is {round(avgtemp,2)}")

print(f"the highest temperature is {np.max(tempOfAWeek)}, the lowest temperature is {np.min(tempOfAWeek)}")

temp_arry = np.array(tempOfAWeek)
fahrenheitArray = temp_arry *9.0/5+32

print(f"the fahrenheit temperature of the week is {fahrenheitArray}")

tempOfAWeek = np.array(tempOfAWeek)
over20Days = np.where(tempOfAWeek > 20)

print(over20Days)
