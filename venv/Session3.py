# Conditions
# Ladder if/else
olaShared = 1
olaMicro = 2
olaMini = 3
olaSedan = 4
olaBike = 5

print("1 -> OLA Shared")
print("2 -> OLA Micro")
print("3 -> OLA Mini")
print("4 -> OLA Sedan")
print("5 -> OLA Bike")
choice = int(input("What Cab would you like to ride"))

if choice == olaShared:
    print("OLA Shared Booked. Please Pay Rs.50")
elif choice == olaMicro:
    print("OLA Micro Booked. Please Pay Rs.100")
elif choice == olaMini:
    print("OLA Mini Booked. Please Pay Rs.150")
elif choice == olaSedan:
    print("OLA Sedan Booked. Please Pay Rs.200")
elif choice == olaBike:
    print("OLA Bike Booked. Please Pay Rs.30")
else:
    print("Please Select Valid Cab and Try Again")


# No Switch Case :)
# Explore : Why not switch case ?
# Is switch case better or ladder if lese is better ?