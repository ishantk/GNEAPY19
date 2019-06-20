# Type of Object
class Order:

    # Constructor
    def __init__(self):
        # print(">> init executed")
        # print("self is:",self)
        self.oid = 0
        self.customerName = "NA"
        self.dishes = 0
        self.price = 0

    # OVER-WRITING : Updated the old constructor with a new one
    def __init__(self, oid, name, dishes, price):
        self.oid = oid
        self.customerName = name
        self.dishes = dishes
        self.price = price


# Rule : When object will be created, init will be executed
#        and self will contain its hashcode

# Object Construction Statement
o1 = Order(1, "John", 5, 1250)
print("o1 is:",o1)

print()

o2 = Order(2, "Fionna", 3, 730)
print("o2 is:",o2)

# We can add any additional attribute later if needed
o2.membership = "prime"

# We can also delete some attribute which was in the object
del o1.customerName

print()
print("o1 data:",o1.__dict__)
print("o2 data:",o2.__dict__)