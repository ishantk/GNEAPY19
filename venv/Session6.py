# Multi Value Container
# If we have list, tupe, set and dictionary available as MVC
# Why we need to create another MVC
# So that we can customize

# Type Creation
class Order:
    pass

# Object Construction Statement
# o1 and o2 are not objects as they contain HashCode of Object
# They are know as Reference Variables
o1 = Order()
o2 = Order()
o3 = o1     # Reference Copy

# To check HashCode for Objects simply print the ref var
print("o1 is:",o1)
print("o2 is:",o2)

# As of now objects has no data :)
# They are Empty Objects or Empty Containers
# to view data in object use __dict__
print("o1 data:",o1.__dict__)
print("o2 data:",o2.__dict__)
print("o3 data:",o3.__dict__)

# Write Data in Object
o1.oid = 1
o1.customerName = "John"
o3.price = 1250
o1.dishCount = 7

o2.oid = 3
o2.deliveryPersonName = "George"
o2.amount = 350
o2.dishes = 3

print("o1 data:",o1.__dict__)
print("o2 data:",o2.__dict__)
print("o3 data:",o3.__dict__)
