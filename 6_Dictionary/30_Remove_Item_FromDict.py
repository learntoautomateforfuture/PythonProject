# pop() method - removes the item with the specified key name
dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
    "year": 1989,
    "carmodel": "Ford"
}
dict1.pop("year")
print(dict1)

# popitem() method - removes the last inserted item
dict2 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
    "year": 1989,
    "carmodel": "Ford"
}
dict2.popitem()
print(dict2)

# clear() method - empties the dictionary
dict3 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
    "year": 1989,
    "carmodel": "Ford"
}
dict3.clear()
print(dict3)

# Del keyword - removes the item with the specified key name,
# also deletes the dict completely
dict4 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
    "year": 1989,
    "carmodel": "Ford"
}
del dict4["age"]
print(dict4)

del dict4