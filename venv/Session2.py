"""
    Model View Controller Architecture

    Model : Data
    View  : UI
    Controller : Logic

    Uber/Ola
    Model : source location, destinition location, type of cab, user data
    View  : User Interface
    Controller : Finding Shortest path with least traffic

    Most of PL's can help us to create above 3

    Model
        Storage Container
        1. Single Value Container
        2. Multi Value Container
            Hetro
            Homo



"""
# Model : Single Value Container

# Container Creation Operation/Instruction
instagramUserName = "auribises"
johnsAge = 30
pi = 3.14

# Reading Type of Container
print(type(instagramUserName))
print(type(johnsAge))
print(type(pi))

# Update Data in Container
johnsAge = 45

# Read Data from Container
print(instagramUserName)
print("john is",johnsAge,"years old")
print(pi)

# Delete Containers
# del instagramUserName
# del pi

# print(instagramUserName) -> error

# Read HashCode of Containers
# print("instagramUserName HashCode:",id(instagramUserName))
# print("johnsAge HashCode:",id(johnsAge))
# print("pi HashCode:",id(pi))

# print("instagramUserName HashCode:",bin(id(instagramUserName)))
# print("johnsAge HashCode:",bin(id(johnsAge)))
# print("pi HashCode:",bin(id(pi)))

# print("instagramUserName HashCode:",oct(id(instagramUserName)))
# print("johnsAge HashCode:",oct(id(johnsAge)))
# print("pi HashCode:",oct(id(pi)))

print("instagramUserName HashCode:",hex(id(instagramUserName)))
print("johnsAge HashCode:",hex(id(johnsAge)))
print("pi HashCode:",hex(id(pi)))


# instagramUserName, johnsAge and pi are Reference Variables
# They hold HashCode of Data !!










