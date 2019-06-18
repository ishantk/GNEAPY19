# A function with single expression is known as Lambda
def fun(n1, n2):
    return n1 * n2

# Lambda Expression
lm = lambda n1, n2 : n1 * n2

print(fun(10, 2))
print(lm(10, 2))

print("fun is:",fun)
print("lm is:",lm)