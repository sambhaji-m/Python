
price = 10000                  # House parice
buyer_credit = False            # buyer credit good or bad

if buyer_credit == True:       # if good creadit
    price = (price * 0.1)


elif buyer_credit == False:    # if bad credit 
    price = (price * 0.2)

print(f"Down payment: {price}") # print downpayment





age = int(input("enter your age: "))

if age >= 18:
    print("yes")

else:
    print("no")



