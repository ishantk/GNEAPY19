# Built In Functions on String
# Strings are IMMUTABLE. They Cannot be changed
# Whenever we perform modification on String a new String is created in memory
"""
name = "Fionna Flynn"
newName = name.upper()
print("name is: ",name, hex(id(name)))
print("newName is: ",newName, hex(id(newName)))
"""
name = "Fionna Flynn"
print("name before is: ",name, hex(id(name)))
name = name.upper()
print("name after is: ",name, hex(id(name)))