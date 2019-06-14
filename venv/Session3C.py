# f(x) = x * (18 / 100)

# billAmount -> Input or Argument
def calculateTaxesOnBill(billAmount):
    tax = billAmount * (18 / 100)
    print("For {} amount taxes are {}".format(billAmount, tax))

print("calculateTaxesOnBill: ",calculateTaxesOnBill)

def calculateTaxesOnBill(billAmount):
    tax = billAmount * (18 / 100)
    return tax

print("calculateTaxesOnBill: ",calculateTaxesOnBill)

print(calculateTaxesOnBill(2000)) # Execution Command
print(calculateTaxesOnBill(100))
result = calculateTaxesOnBill(300)
print(result)
