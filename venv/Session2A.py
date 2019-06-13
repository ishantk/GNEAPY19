# Model : Multi Value Container

# pixel = (125, 200, 101)
# marks = (90, 80, 70)
# data = ("john", 20, "jennie", 30)
#
# print(pixel, type(pixel), id(pixel))
# print(marks, type(marks), hex(id(marks)))
# print(data, type(data), id(data))

# Tuple is a Multi Value Container : IMMUTABLE

# pixel, marks and data are Reference Variables
# They hold HashCode of Data !!

# List is a Multi Value Container : MUTABLE

# pixel = [125, 200, 101]
# marks = [90, 80, 70]
# data = ["john", 20, "jennie", 30]
#
# print(pixel, type(pixel), id(pixel))
# print(marks, type(marks), hex(id(marks)))
# print(data, type(data), id(data))

# Set is a Multi Value Container : MUTABLE | UNIQUE
# pixel = {125, 200, 101, 200}
# marks = {90, 80, 70, 90, 90, 80}
# data = {"john", 20, "jennie", 30, "john", 30}
#
# print(pixel, type(pixel), id(pixel))
# print(marks, type(marks), hex(id(marks)))
# print(data, type(data), id(data))

# Dictionary
students = {"john":30, "jennie":20, "jack":22}
print(students)
print(type(students))
print(id(students))