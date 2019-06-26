import matplotlib.pyplot as plt

"""
    f(X) = X
    x : 1 | Y : 1
    x : 2 | Y : 2
    .
    ..
    
    f(X) = X*X
    X : 1 | Y : 1
    X : 2 | Y : 4
"""

"""
Y = [10, 20, 90, 30, 70]
plt.plot(Y)
plt.show()
"""

X = list(range(1,11))
print(X)

Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

print(Y1)
print(Y2)
print(Y3)

# plt.plot(X, Y1)
# plt.plot(X, Y2)
# plt.plot(X, Y3)

plt.plot(X, Y1, label="Y1")
plt.plot(X, Y2, label="Y2")
plt.plot(X, Y3, label="Y3")

plt.legend()

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("Polynomial Graphs")
plt.grid(True)

plt.xlim(0, 10)
plt.ylim(0, 1000)

plt.savefig("Graphs")

plt.show()