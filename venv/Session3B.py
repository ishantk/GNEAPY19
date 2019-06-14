# Function/Procedure/Method/Routine
# Function : is a Block which contains commands
#            commands will be executed line by line
#            function has a name of your choice followed by ()
def calculateTaxesOnBill():
    billAmount = float(input("Please Enter Amount: "))
    tax = billAmount * (18 / 100)
    print("For {} amount taxes are {}".format(billAmount, tax))


n = int(input("How many bills you wish to process? "))

for i in range(1, n+1, 1):
    calculateTaxesOnBill() # Execution Command for Function

print("Thank You !!")


calculateTaxesOnBill()