import os

path = os.getcwd()
print("path is:",path)

print(os.name)
print(os.getlogin())
print(os.getppid())

path = "/Users/ishantkumar/Downloads/orders.csv"
print("Is path exisiting: ",os.path.exists(path))
print("Is path a Drirectory: ",os.path.isdir(path))
print("Is path a File: ",os.path.isfile(path))

path = "/Users/ishantkumar/Downloads"

files = os.walk(path)
allFiles = list(files) # Convert into a list
for file in allFiles:
    print(file)


# Assignment
# List all the files for Documents, Music and Videos