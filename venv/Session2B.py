# Controller : Logic to solve Problem
# 1. Operaotrs 2. Conditions 3. Loops

# 1. Operators
# Arithmetic Operators : +, -, *, /, %, //, **
result = 10 // 3
result = 2 ** 3
print(result)

# Assignment Operators : =, +=, -=, *=, /=, %=, //=, **=
age = 30 # Data Write Operation
age = 33 # Update Operation

result += age # result = result + age
print(result)
print(age)

# Conditional Operators : >, <, >=, <=, ==, !=
print(result<age)

# Logical Operators : and or not
# print(10>5 and 2>13)
print(10>5 or 2>13)

# Membership Operators : is in
phonePrice = 30000
print(phonePrice is 30000) # is vs ==
print(phonePrice is not 20000)

marks = [10, 20, 30]
print(100 in marks)
print(100 not in marks)

# Explore Bitwise Operators on Negative Numbers
# Bitwise Operators : &, |, ~, >>, <<
num1 = 8                   # 1 0 0 0
num2 = 12                  # 1 1 0 0
num3 = num1 & num2         # 1 0 0 0
num4 = num1 | num2         # 1 1 0 0
num5 = num1 >> 2           # 1 0 0 0 >> 2
                           # _ _ 1 0 -> 0 0 1 0
print(num3)
print(num4)
print(num5)










