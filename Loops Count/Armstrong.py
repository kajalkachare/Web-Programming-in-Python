#Python Program to Check Given Number is Armstrong or not
'''
Armstrong Number-> means the sum of cubes of each digit is equal to number itself.
'''

num=int(input("Enter The Number: "))
sum=0
temp=num
while temp > 0:
    digit= temp%10
    sum+= digit**3
    temp//= 10
if sum== num:
    print(num,"is Armstrong Number.")
else:
    print(num,"is not Armstrong number.")