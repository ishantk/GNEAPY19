# file = open("/Users/ishantkumar/Downloads/MyApp.py", "r")
file = open("Session7.py","r")

# data = file.read()
# print(data)
#
# print(type(data)) # str

lines = file.readlines()
print(lines)
print(type(lines)) # list

count = 0

# Source Code Analysis
# Iterate in List
for line in lines:
    print(line)
    if line.startswith("#"):
        count = count + 1

print("Comments with# are",count,"in number")

"""
    Find how many classes and functions are in the Python file

"""