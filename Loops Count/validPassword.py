#Python program to check validity of passwords by user inputs
'''
1] Check lower case letter
2] Check Upper Case Letter
3] Check The digit Number
4] Check the Special Characters
and 5] Check length atleast 6 characters
'''
#re is a RegularExpression (RegEx)
import re
flag=0
password=input("Enter The Password: ")
if not re.search('[a-z]',password):
    flag=1

if not re.search('[0-9]', password):
    flag=1

if not re.search('[A-Z]', password):
    flag=1

if not re.search('[@$!#]', password):
    flag=1

if len(password)<6:
    flag=1

if flag==0:
    print("Password is Valid")
else:
    print("Password is invalid")
