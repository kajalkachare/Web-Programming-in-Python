#Python program that reads the product code and order the amount and print bill amount

code=int(input("Enter the product code 1,2,3:? "))
amount=int(input("Enter the amount: "))
if code==1:
    if amount > 1000:
        discount= amount* 0.1
    else:
        discount=0
elif code==2:
    if amount >100:
        discount = amount * 0.05
    else:
        discount=0
elif code==3:
    if amount > 500:
        discount= amount* 0.1
    else:
        discount=0
else:
    print("product is not Available")
bill_amt= amount-discount
print("Customer has to pay:",bill_amt)





