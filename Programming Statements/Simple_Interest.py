#Python Program to find Simple Interest

P= int(input("Enter The principle Amount"))
T= float(input("Enter the Time Period"))
R= float(input("Enter the Rate of Interest"))
SI= (P*T*R)/ 100
print("print simple interest",SI)


#2nd Way(By using function)
def simple_interest(p,t,r):
    print('The Principal Amount is: ',p)
    print('The Time period is: ',t)
    print('The Rate of interest: ',r)
    si= (p*t*r)/100
    print('The simple interest is: ',si)
P=int(input("Enter the Principal amount: "))
T=int(input("Enter the Time Period: "))
R=int(int(input("Enter the Rate of interest: ")))
simple_interest(P,T,R)
