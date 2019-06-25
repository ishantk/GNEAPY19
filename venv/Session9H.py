import pandas as pd

table = pd.read_csv("CityTemps.csv")
print(table)
print("=========")
print(table["Ludhiana"])
print("========")
# print(table.iloc[1])
print(table.iloc[1:5])

print()
print("Count is:")
print(table.count())