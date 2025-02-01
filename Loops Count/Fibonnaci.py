# Python Program to print 0 to 50 fibonacci series number
'''
Fibonacci numbers means sum of the previous numbers of the sequence.
'''

def Fibonacci_series(limit):
    a=0
    b=1
    while a <= limit:
        print(a,end=" ")
        a, b = b, a + b

# Call function to print Fibonacci numbers up to 50
Fibonacci_series(50)



