class Order:

    def __init__(self, oid, name, dishes, price):
        self.oid = oid
        self.customerName = name
        self.dishes = dishes
        self.price = price

    def showOrderDetails(self):
        print("******************")
        print("OID\t\t",self.oid)
        print("NAME\t", self.customerName)
        print("DISHES\t", self.dishes)
        print("PRICE\t", self.price)
        print("******************")


"""
o1 = Order(1, "John", 3, 500)
o2 = Order(2, "Fionna", 5, 700)
# print(o1.__dict__)
o1.showOrderDetails()
o2.showOrderDetails()
"""

"""
o1 = Order(None, None, None, None)

o1.oid = int(input("Enter Order ID: "))
o1.customerName = input("Enter Cutomer Name: ")
o1.dishes = int(input("Enter Dishes in Order: "))
o1.price = int(input("Enter Price of Order: "))

o1.showOrderDetails()

"""

# Let us create as many as order objects which we wish to create
choice = "yes"
orders = [] # Empty List
while choice == "yes":
    oRef = Order(None, None, None, None)

    oRef.oid = int(input("Enter Order ID: "))
    oRef.customerName = input("Enter Cutomer Name: ")
    oRef.dishes = int(input("Enter Dishes in Order: "))
    oRef.price = int(input("Enter Price of Order: "))

    orders.append(oRef)

    choice = input("Do you wish to add another Order(yes/no)")

print()

for o in orders:
    o.showOrderDetails()

# Lab Assignment : Sort the List of Order Objects based on Price
#                  Sort the List of Order Objects based on dishes