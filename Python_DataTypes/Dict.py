'''
Dictionary-collection of key value pairs
key- unique,immutable(tuple,string)
1. value- it can repeat or any datatype,not be unique
2.Creating a dictionary
using curly braces({})
dict function -dict()
'''

student={"name":"Kajal","age":20}
employee=dict(id=24,name="kajal")
print(student)
print(employee)
print(type(student))
print(type(employee))

#dictionary functions
#keys()
print(student.keys())

#values()
print(student.values())

#items() it will return key value pair as tuple
print(student.items())

#get() it will return value of a given key
print(student.get("name"))

#update() it will update the dict with new pair
student.update({"name":"Kavya"})
print(student)

#pop it will remove the key value pair
student.pop("name")
print(student)

#traversing in a dictionary -iterating over a dict
student={"name":"Kajal","age":20,"city":"Mumbai"}
for key in student:
    print(f"key:{key},values:{student[key]}")
print("============================================")
for key,value in student.items():
    print(f"key:{key},values:{value}")

'''diff btw dictionary and list
dictionary collection of key value pair
list is ordered collection of items
2.dictionary  defined using {} and list []
3.In Dictionary keys are unique values can be duplicate
list allow duplicate values.
'''
