# copy() method is used to make a copy of a dictionary
dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
mydict = dict1.copy()
print(mydict)

# dict() method is also used to make a copy of a dictionary
dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
mydict = dict(dict1)
print(mydict)

# Nested Dictionaries
nestedDict = {'person1': {'name': 'tom', 'age': 40},
              'person2': {'name': 'jerry', 'age': 40},
              'person3': {'name': 'jack', 'age': 40}}
print(nestedDict)