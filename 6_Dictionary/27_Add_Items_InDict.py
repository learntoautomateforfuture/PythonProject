"""
Adding an item to the dictionary is done by using a new index
key and assigning a value to it
"""
dict1 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
dict1["model"] = "sunny"
print (dict1)

"""
update() method: update the dictionary with the items from a given argument. 
If the item does not exist, the item will be added.
The argument must be a dictionary, or an iterable object with key:value pairs.
"""

dict2 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
dict2.update({"carmodel": "Ford"})
print (dict2)