"""
Tuple are used to store multiple items in a single variable.
Created using round brackets
Tuple items are indexed, starts with [0]
Items in the tuple can be of any datatype

Tuple items are ordered, unchangeable(Immutable), and allow duplicate values.
	- Ordered : that the items have a defined order, and that order will not change.
	- unchangeable : we cannot change, add or remove items after the tuple has been created.
	- Allow duplicate values: tuple can have items with the same value
"""

tuple1 = ("Apple", "Banana")
tuple2 = (89, 4, 90, 675)
tuple3 = ("Apple", "Banana", 89, 4.8, True, 89)
print (tuple1)

# len() method is used to find the no:of items in the tuple
print (len(tuple1))

tuple3 = ("Apple", "Banana", 89, 4.8, True, 89)
print (tuple3[3])

"""
To create a tuple with only one item, 
you have to add a comma after the item, otherwise Python will not recognise it as a tuple
"""
tuple2 = (("ABC", ))
print (tuple2)
print (type(tuple2))

# tuple() constructor to make a tuple
tuple3 = tuple(("Apple", "Banana", 89))
print (tuple3)


