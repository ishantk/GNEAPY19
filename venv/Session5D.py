"""
    Client Requirement:
    -------------------
    User should register in my software
    User should tell me what goods he wants to ship
    Who is the Sender
    What is the type of Shipment (Basic/Express)


    Client Requirement:
    -------------------
    User should register in my software
    User should be able to add food items in the cart
    User should send a request ot Restaurant
    Restaurant will confirm Order and Deliver Person will deliver

    Extract those terms which have data associated with it
    data associated is details of that term

    eg:
    User        -> Object
        name    -> Attributes
        phone
        email
        address
        age
        gender
        .
        ..
        ....

    FoodItem
        name
        type
        price
        quantity
        .
        ..
        ....

    Restaurant
        name
        address
        type
        openingTime
        closingTime
        .
        ..
        ...

    Rule : Extract as much as Terms you can
           Associate as many as details with Term


   OOPS : Object Oriented Programming Structure
          Object and Class


          Real World:
            Object
            Anything which exists in reality is an Object
            Class
            Drawing of an Object

            1. Think of an Object
            2. Draw the Object i.e. by class
            3. Create the Real Object from class

          Computer Science:
            Object is a Multi Value Container
            Its a BOX
            It can be homogeneous or hetrogeneous

            Class represents its type


"""

# Type Creation by us i.e. Developer
class User:
    pass

class FoodItem:
    pass

class Restaurant:
    pass

# Object Construction Statement
u1 = User()
u2 = User()

print(u1)
print(u2)

# u1 and u2 are not objects
# u1 and u2 contains HashCode of Object
# u1 and u2 are called reference variables


# Write Data in Object / Create Attributes in Object
u1.name = "John"
u1.phone = "+91 99999 88888"
u1.email = "john@example.com"
u1.age = 30

u2.name = "Fionna"
u2.vehicle = 3
u2.salary = 30000

# See Data in Your Objects
print(u1.__dict__)
print(u2.__dict__)

# Update Attributes in Object
u1.name = "John Watson"
u2.salary = 75000

print()

print(u1.__dict__)
print(u2.__dict__)

del u1.email
del u2.salary

print()

print(u1.__dict__)
print(u2.__dict__)

"""
    1. Add Data in Object       u1.name = "John"
    2. Update Data in Object    u1.name = "John Watson"
    3. Delete Data in Object    del u1.name
    4. View Data in Object -> __dict__
"""