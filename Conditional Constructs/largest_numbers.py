#python program to find Largest Among 3 Numbers

Num1=float(input("Enter First Number : "))
Num2=float(input("Enter Second Number : "))
Num3=float(input("Enter Third Number : "))
if Num1 > Num2 and Num1 > Num3:
    print("First Number is Largest")
elif Num2 > Num1 and Num2 > Num3:
    print("Second Number is Largest")
else:
    print("Third Number is Largest")

