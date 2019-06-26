import json

# Python Dictionary
student = {"roll":101, "name":"John", "age":20}
print(student)
print(type(student))

print()

# JSON is textual i.e. string representation of dictionary
# Converting Dictionary into JSON
jsonData = json.dumps(student)
print(jsonData)
print(type(jsonData))

print()

# Converting JSON into Dictionary
dictionaryData = json.loads(jsonData)
print(dictionaryData)
print(type(dictionaryData))