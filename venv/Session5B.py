student1 = {"roll":1, "name":"John", "age":20}
student2 = {"roll":12, "name":"Fionna", "age":22}

# Dictionary is combination of keys and Values
print(len(student1))
print(max(student1))
print(min(student1))


# To get the value you must know the key
print(student1["name"])
print(student2["age"])

# Explore -> JSON (Combination of Dictionary and Lists)

# We can obtain all the keys:
keys = student1.keys()
print(keys, type(keys))

for key in keys:
    print(key, student1[key])

values = student2.values()
print(values)