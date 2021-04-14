"""
Lists are used to store multiple items in a single variable.
Created using square brackets - []
List items are indexed, starts with [0]
Items in the list can be of any datatype

List items are ordered, changeable(mutable), and allow duplicate values.
 	- Ordered : new items  are always added at the end of the list
	- Changeable : we can change, add, and remove items in a list after it has been created.
	- Allow duplicate values: lists can have items with the same value
"""
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
List4 = ['apple', 89, False, 89.1, 89]
print (list1)

# len() method is used to find the no:of items in the list
list1 = ["apple", "banana", "cherry"]
print (len(list1))

# list() - constructor is also used to create list
# note the double round-brackets
listconst = list(("Apple", 8, 8.9, True))
print (listconst)







