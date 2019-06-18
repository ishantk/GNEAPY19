def sum(num1, num2):
    return num1 + num2

print("1. sum is:",sum)

# OVER-WRITING the FUNCTION

# def sum(num1):
#     return num1 + 10

print("2. sum is:",sum)

result = sum(10, 20)
print("Result is:",result)

print("sum is:",sum)

# Reference Copy
fun = sum # Alias

print("fun is:",fun)

result = fun(11, 22)
print("Result is:",result)