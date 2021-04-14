# Can change the value of a specific item by referring to its key name
dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
dict1["year"] = 1989
print(dict1)

"""
* update() method - will update the dictionary with the items 
from the given argument. 
* The argument must be a dictionary, or an iterable object 
with key:value pairs
"""

dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
dict1.update({"endyear" :"2025"})
print(dict1)