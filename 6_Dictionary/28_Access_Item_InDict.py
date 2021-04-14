"""
Can access the items of a dictionary by referring
to its key name, inside square brackets
"""
dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
x = dict1["age"]
print (x)

# get() method is also used to get the value by giving the key
x1 = dict1.get("name")
print (x1)

# keys() method will return a list of all the keys in the dictionary
keyNames = dict1.keys()
print (keyNames)

# values() method will return a list of all the values in the dictionary
valueNames = dict1.values()
print (valueNames)

# items() method will return each item in a dictionary, as tuples in a list
Items = dict1.items()
print (Items)