"""
Dict are used to store data values in key:value pairs
Dict are written with curly brackets, and have keys and values
Items in the dict can be of any datatype

Dict items are ordered, changeable, and does not allow duplicates.
  - Ordered : Items have a defined order, and that order will not change.
  - changeable : We can change, add or remove items after the dictionary has been created
  - Do not allow duplicate values : Dict cannot have two items with the same key
"""
dict1 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# len() method is used to find the no:of items in the set
print (len(dict1))

# Check if specified key is present in the dict using ‘in’ keyword
dict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in dict2:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")