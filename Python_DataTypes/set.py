'''
Set-> unsorted collection of unique elements in python
it is unique,
unordered
mutable
'''

#creating a set
set1={1,2,3,4,5,6,3,2}
print(set1)

#way2 :set()function
set2=set([2,4,6,2,3,8,20])
print(set2)

set3={20}
print(set3)
print(type(set3))
print(type(set3))

#creating a empty set
set4={}  #wrong way
print(set4)
print(type(set4))

print("=============================================")
set5=set()  #correct way
print(set5)
print(type(set5))

#add()
set1.add(100)
print(set1)

#remove() if element not found it gives error
# set1.remove(2)
# print(set1)

#discard()
set1.discard(2)  #if element not found ,it doesnt throw error
print(set1)

#pop()
set1.pop()  #random element remove
print(set1)

#clear()
set1.clear()
print(set1)

set1={1,2,3,}
set2={3,4,5}
print("union:",set1 | set2)  #union

#Itersection
print("Intersection:",set1 & set2)

#symmetric difference()
print("symmetric difference:",set1 ^ set2)

#Difference()
print("Difference : ",set1-set2)

setA={1,2,3}
setB={1,3}
print("subset:",setB.issubset(setA))

'''
why to use Set and when to use Set?
1.if i want any unique element,we use set
2.quikly check if element exist or not
3.efficient execution of set operation such has union,Intersection
'''