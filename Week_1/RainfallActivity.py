import numpy as np

# Sample rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

# Tasks: 
# Convert the list to a NumPy array and print it.
# Print the total rainfall for the week.
# Print the average rainfall for the week.
# Count how many days had no rain (0 mm).
# Print the days (by index) where the rainfall was more than 5 mm.
# Calculate the 75th percentile of the rainfall data and identify values above it. (help : use numpy.percentile())


rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
npRainfall = np.array(rainfall,dtype=np.longdouble)

print(npRainfall)

totalRainfall = np.sum(npRainfall)
print(f" the total rainfall is {totalRainfall}")

avgRainfall = np.average(npRainfall)
print(f"the average rainfall is {np.around(avgRainfall,2)}")

days = np.count_nonzero(npRainfall)
print(f"there are {npRainfall.size-days} days have no rainfall")

print(f"These days rainfall was great than 5mm : {np.nonzero(npRainfall>5)}")

percentile_75 = np.percentile(npRainfall,75)

print(f"percentile_75 is {percentile_75}")

abovePersontile75Days = np.where(npRainfall>percentile_75)
print(f"the days above percentile_75 is {abovePersontile75Days}")

