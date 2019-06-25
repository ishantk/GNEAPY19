# import numpy
import numpy as np

numbers = [10, 20, 30, 40, 50]
print(numbers)
print(type(numbers))

# Arrays in NumPy
arr1 = np.array([10, 20, 30, 40, 50])
print(arr1)
print(type(arr1))

arr2 = np.array({10, 20, 30, 40, 50})
print(arr2)
print(type(arr2))

arr3 = np.array((10, 20, 30, 40, 50))
print(arr3)
print(type(arr3))

employee = {"eid":1, "name":"John", "salary":30000}
arr4 = np.array(employee)
print(arr4)
print(type(arr4))

name = "John"
arr5 = np.array(name)
print(arr5)
print(type(arr5))
