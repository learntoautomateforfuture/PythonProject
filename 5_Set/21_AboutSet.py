"""
Sets are used to store multiple items in a single variable.
Created using curly brackets
Set items are not indexed
Items in the set can be of any datatype

Set items are unordered, unchangeable(Immutable), and does not allow duplicate values.
    - Unordered : Items in a set do not have a defined order, Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
	- Unchangeable : we cannot change the items after the set has been created
 	- Do not allow duplicate values : Sets cannot have two items with the same value.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
Set4 = {"abc", 34, True, 40, "male"}

# len() method is used to find the no:of items in the set
print (len(set1))

# set() constructor to make a set
set5 = set(("Apple", "Banana", 89))
print (set5)