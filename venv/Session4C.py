languages = ["C", "C++", "Java", "Python", "Go"]
languages[1] = "Ruby" # Update Operation
print(languages)

del languages[2] # Delete Operation
print(languages)

print(languages[2]) #

print(languages[-3])

languages.pop(1) # remove index #1
print(languages)

languages.remove("Go")

print(languages)

names = ["John", "Jennie", "Jim", "John", "Jack"]
# names.remove("John")
# del names["John"] # Will Not Work
del names[0]
print(names)