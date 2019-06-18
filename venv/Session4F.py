cart = []

choice = "yes"

while choice == "yes":
    item = input("Add Food Item in Your Cart: ")
    cart.append(item)
    choice = input("Would you like to add more items(yes/no): ")


print("Items Added: ",cart)

# Sort Food Items in Cart in Ascending Order
# without any in built function

for i in range(0, len(cart)):
    print(cart[i])

# Enhanced For Loop OR For-Each Loop
for elm in cart:
    print(elm)

# Explore Same Functions as Discussed in Tuple and Set :)