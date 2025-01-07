'''
list -> list is collection of items that can store multiple data.
- Lists are one of the most commonly used data structures in Python.
- List are Ordered, Mutable.
list are defining in [] bractes.
'''

#creating a list
list=[1,2,3,4,5]
print(list)
print(type(list))

#concatination -> add two list
list1=[1,2,3,4,5,6]
list2=[7,8,9]
print(list1+list2)

#repetation
list3=[1,2,3,4,5,6]
print(list3*3)

#membership
list4=[1,2,3,4,5,6,4,8,9]
print(3 in list4)    #True
print(1 not in list4)  #False

'''Slicing Lists-> Slicing allows you to extract a portion of a list. 
- The syntax for slicing is list[start:stop:step], 
where start is the index to start from, stop is the index to stop before,
and step is the step size.
'''
#List Slicing
list=[1,23,75,78,2,34,9]
print(list[1:5])
print(list[:6])
print(list[:])
print(list[::2])
print(list[::-1])

#Modifying Lists
#-Lists are mutable, so you can change their elements
my_list=[1,2,3,4]
my_list[2]=99
print(my_list)    # Change the third element to 99

#List Functions
'''
1] len()-> Returns the number of items in a list
2] append()-> Adds an item to the end of the list.
3] extend() -> Extends the list by appending elements from another iterable.
4] insert() ->Inserts an item at a specified position in the list.
5] remove()-> Removes the first occurrence of a specific value from the list.
6] pop()-> Removes and returns an item at a specified index.
7] index()->Returns the index of the first occurrence of a specific value.
8] count()-> Returns the number of times a specific value appears in the list.
9] sort()-> Sorts the list in ascending order.
10]sum()-> adding all the elements 
'''
#len()
list5=[1,2,3,4,6,5,8,9]
print(len(list5))

#max()
list5=[1,2,3,4,6,5,8,9]
print(max(list5))

#min()
list5=[1,2,3,4,6,5,8,9]
print(min(list5))

#sum()
list5=[1,2,3,4,6,5,8,9]
print(sum(list5))

#sorted()
list5=[1,2,3,8,9,4,6,5]
print(sorted(list5))

#append()
fruits =["Apple","Pineapple","Orange","Banana"]
fruits.append("Grapes")
print(fruits)
print(type(fruits))      # <class 'list'>

#insert()
fruits =["Apple","Pineapple","Orange","Banana"]
fruits.insert(1,"Banana")
print(fruits)

#remove()
fruits =["Apple","Pineapple","Orange","Banana"]
fruits.remove("Orange")
print(fruits)

#pop()
fruits =["Apple","Pineapple","Orange","Banana"]
print(fruits.pop(1))
print(fruits)

#index()
fruits =["Apple","Pineapple","Orange","Banana"]
fruits.insert(3,"Grapes")
print(fruits)

#count()
fruits= ['Apple', 'Pineapple', 'Orange', 'Grapes', 'Banana']
print(fruits.count("Apple"))

#reverse()
fruits= ['Apple', 'Pineapple', 'Orange', 'Grapes', 'Banana']
print(fruits.reverse())
print(fruits)

#clear()
fruits= ['Apple', 'Pineapple', 'Orange', 'Grapes', 'Banana']
print(fruits.clear())
print(fruits)

#traversing in list using for loop
colors=["Purple","Red","Blue","Pink","Black"]
for color in colors:
    print(colors)

#traversing in list using for loop with index
colors=["Purple","Red","Blue","Pink","Black"]
for i in range(0,len(colors)):
    print(colors[i])

#traversing in list using while loop
colors=["Purple","Red","Blue","Pink","Black"]
i=0
while i<len(colors):
    print(colors[i])
    i+=1
