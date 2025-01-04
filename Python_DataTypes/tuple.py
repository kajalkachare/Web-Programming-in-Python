'''
tuple -> it is an immutable collection of items. we cannot add,remove or modify,orded
'''

#crete a tuple
# name=("kajal","Kavya","kinjal")
# print(name)
# print(type(name))
# tuple=(28 ,)
# print(tuple)
# print(type(tuple))

# #traversing in tuple
# name=("kajal","Kavya","kinjal")
# print(name[2])
# print(name[-1])

#concatation
a=(1,2,3,4,2,5,2)
b=(5,2,7,8)
print(a+b)
print(a*2)
print(10 in a)
print(12 not in a)
print(len(a))
print(max(a))
print(min(a))
print(a.count(2))
print(a.index(2))

#slicing
a1=[1,2,3,4,5,6,10,4]
print(a1[1:4])

#reverse
print(a1[::-1])
'''
why we use tuple?
1] tuple is faster then list
2] tuple ensures the integrity of data 
'''