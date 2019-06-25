import numpy as np
A = [10, 20, 30, 40, 50]
arr1 = np.array(A)
print(arr1)
print(arr1.shape)


B = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
arr2 = np.array(B)
print(arr2)
print(arr2.shape)

C =[
        [
            [10, 20],
            [40, 50],
            [70, 80]
        ],
        [
            [10, 20],
            [40, 50],
            [70, 80]
        ]
    ]

arr3 = np.array(C)
print(arr3)
print(arr3.shape)

print("************")

# arr4 = np.zeros(8)
arr4 = np.ones(8)
print(arr4)
print(arr4.shape)

# IMMUTABLE
arr5 = arr4.reshape(2, 2, 2)
print(arr5)
print(arr5.shape)

# Flatten Array
arr6 = arr5.ravel()
print(arr6)
print(arr6.shape)

# Assignment :
# Create a numpy array of 1s and 0s
# representing 8 X 8 Chessboard
# Ask input from user where he wants to place the Queen
# example : 2,3 | 5,5 etc
# Check if user has entered an incorrect number
# Make that element as 9 where queen will be placed
"""
1   9   1   0
0   1   0   1
1   0   1   0
0   1   0   1

"""

