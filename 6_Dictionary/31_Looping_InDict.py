# To print all key names in the dictionary, one by one
dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
for x in dict1:
    print(dict1)

# Print all values in the dictionary, one by one
dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
for x in dict1:
    print(dict1[x])

# values() method to return values of a dictionary
dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
for x in dict1.values():
    print(x)

# keys() method to return the keys of a dictionary
dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
for x in dict1.keys():
    print(x)

# Loop through both keys and values, by using the items() method
dict1 = {
    "name": "Tom",
    "age": 35,
    "number": 175,
}
for k, v in dict1.items():
    print(k, v)