import numpy as np
arr = np.genfromtxt("CityTemps.csv", delimiter=",")
print(arr)
print("========")
print(arr[1])
print("========")
print(arr[1][0])
print(arr[1][1])
print(arr[1][2])

# Project Work:
# Analyse CityTemps.csv file
# Find the City with maximum temperature and minimum temperature
# Also tell the month and year when the temperature was max and min
