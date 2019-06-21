class Customer:

    # Constructor
    def __init__(self, name="NA", phone="NA", email="NA"):
        self.name = name
        self.phone = phone
        self.email = email


c1 = Customer()
# print(c1.__dict__)

c1.name = input("Enter Customer Name: ")
c1.phone = input("Enter Customer Phone: ")
c1.email = input("Enter Customer Email: ")

# print(c1.__dict__)

# Problem : Whatever data you add in object will be temporary
#           Because object will be deleted automatically and data will be lost

# Solution:
# Persistence
#   1. Save Data in Files
#   2. Save Data in DataBase

# Object Relational Mapping | ORM
# To create table see the struture of your Object :)
# Type of Object i.e. Class Name will be the Table Name
# Columns in the Table will be those which are attributes of your Object
# Customer -> Table Name
# name phone and email are column names
# Table can have 1 extra column to uniquely identify a row
# That column is primary key


choice = input("Would you like to save Customer (yes/no):")
if choice == "yes":
    file = open("/Users/ishantkumar/Downloads/customers.csv", "a")

    # CSV Format Data
    data = "{},{},{}\n".format(c1.name,c1.phone, c1.email)

    file.write(data)

    file.close()



