import matplotlib.pyplot as plt

X = list(range(1,11))
print(X)

Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

# plt.plot(X, Y1, "y")
# plt.plot(X, Y2, "m")
# plt.plot(X, Y3, "b")

# plt.plot(X, Y1, "o")
# plt.plot(X, Y2, "^")
# plt.plot(X, Y3, "D")

plt.plot(X, Y1, "--")
plt.plot(X, Y2, "-.")
plt.plot(X, Y3, ":")

plt.show()

# https://matplotlib.org/tutorials/index.html
# https://seaborn.pydata.org/
# Explore more datasets in csv formats at kaggle :)

