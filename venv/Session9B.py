import numpy as np

arr1 = np.zeros(8)
arr2 = arr1.reshape(2,2,2)
print("*******")
print(arr2)
print("*******")
print(arr2[0])
print("*******")
print(arr2[0][0])
print("*******")
print(arr2[0][0][0])

arr2[0][0][1] = 99
print("=========")
print(arr2)
print("=========")

# Read Arrays with loops :)


