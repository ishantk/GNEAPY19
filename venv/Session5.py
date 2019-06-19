# Set -> Uniqueness
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7, 5}

print(A)
print(B)

# C = A | B # Union Operation
C = A.union(B)
print(C)

# D = A & B # Intersection Operation
D = A.intersection(B)
print(D)

# E = A - B # Difference Operation
E = A.difference(B)
print(E)

X = {10, 20, 30, 40, 50}
Y = {20, 30}

print("Is Y subset of X", Y.issubset(X))
print("Is X superset of Y", X.issuperset(Y))

# Enhanced For Loop for Set
for elm in X:
    print(elm)