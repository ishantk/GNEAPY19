import pandas as pd

nums = [10, 20, 30, 40, 50]
S1 = pd.Series(nums)

salaries = {"john":30000, "jennie":40000, "jim":50000}
S2 = pd.Series(salaries)

print(S1)

print("..........")

print(S2)

print(S1[4])
print(S2["jennie"])

# Slicing
print()
print("S1[1:]: ",S1[1:])
print()
print("S1[:2]: ",S1[:2])
print()
print("S1[2:5]: ",S1[2:5])
print()

print("S2[john]: ",S2["john":])
print()
print("S2[john:jim]: ",S2["john":"jim"])
print()
