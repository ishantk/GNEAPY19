"""
billAmount = float(input("Please Enter Amount: "))
# GST@18% needs to be calculated
tax = billAmount * (18/100)
print("For {} amount taxes are {}".format(billAmount, tax))

print()

billAmount = float(input("Please Enter Amount: "))
# GST@18% needs to be calculated
tax = billAmount * (18/100)
print("For {} amount taxes are {}".format(billAmount, tax))

print()

billAmount = float(input("Please Enter Amount: "))
# GST@18% needs to be calculated
tax = billAmount * (18/100)
print("For {} amount taxes are {}".format(billAmount, tax))
"""

n = int(input("How many bills you wish to process? "))
# i = 1

"""
while i <= n:
    billAmount = float(input("Please Enter Amount: "))
    tax = billAmount * (18 / 100)
    print("For {} amount taxes are {}".format(billAmount, tax))
    i+=1
"""

# for i in range(0, n):
# for i in range(1, n+1):
# for i in range(1, n+1, 1):
for i in range(1, n+1, 2):
    billAmount = float(input("Please Enter Amount: "))
    tax = billAmount * (18 // 100)
    print("For {} amount taxes are {}".format(billAmount, tax))

print("Thank You !!")