#Python Program to find Leap Year

year= int(input("Enter the  Year: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("Given Year is a Leap Year")
else:
    print(" Not a Leap year")