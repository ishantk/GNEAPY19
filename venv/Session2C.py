# Conditions
amount = int(input("Enter Amount: "))
promoCode = input("Enter Promo Code: ")

if amount>500:
    if promoCode == "Zomato":
        print("We can give you an offer of 40%")
    else:
        print("Please apply Zomato Promo Code")
else:
    print("Please add food items greater than 500 to avail discounts")