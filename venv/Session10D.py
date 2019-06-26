import matplotlib.pyplot as plt
import numpy as np

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y = [11, 7, 12, 34, 5, 12, 19, 17, 23, 13]

X1 = np.random.randn(200)
Y1 = np.random.randn(200)

plt.scatter(X, Y, label="India")

plt.scatter(X1, Y1, label="China")

plt.legend()

plt.show()