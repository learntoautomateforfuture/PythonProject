# add() method - To add one item to a set
set1 = {"apple", "banana", "cherry"}
set1.add("grapes")
print(set1)

# update() method - To add items from another set into the current set
set2 = {"apple", "banana", "cherry"}
set3 = {True, False, False}
set2.update(set3)
print(set2)

# Also, it allows to add object of any iterable (like list, tuple, dict)
set4 = {"apple", "banana", "cherry"}
list1 = ["kiwi", "orange"]
set4.update(list1)
print(set4)
