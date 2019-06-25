import pandas as pd

N1 = [10, 20, 30, 40, 50]
N2 = [11, 21, 31, 41, 51]

DF1 = pd.DataFrame([N1, N2])
print(DF1)

stu1 = {"roll":1, "name":"John", "age":20}
stu2 = {"roll":2, "name":"Fionna", "age":21}

print()

DF2 = pd.DataFrame([stu1, stu2])
print(DF2)

print()
print(DF1[0])
print()
print(DF2["roll"])
print()
print(DF2["name"][1])
