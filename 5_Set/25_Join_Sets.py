# Note: Both union() and update() will exclude any duplicate items.
# union() method - used to join items from two sets and returns a new set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# update() method - inserts all the items from one set into another
setA = {"a", "b" , "c"}
setB = {1, 2, 3}
setA.update(setB)
print(setA)

# intersection_update() - will keep only the items that are present in both sets
x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}
x1.intersection_update(y1)
print(x1)

# intersection() - will return a new set, that only contains the items that are present in both sets
x2 = {"apple", "banana", "cherry"}
y2 = {"google", "microsoft", "apple"}
z2 = x2.intersection(y2)
print(z2)

# symmetric_difference_udpate() - will keep only the elements that are NOT present in both sets
x3 = {"apple", "banana", "cherry"}
y3 = {"google", "microsoft", "apple"}
x3.symmetric_difference_update(y3)
print(x3)

# symmetric_difference() - will return a new set,
# that contains only the elements that are NOT present in both sets
x4 = {"apple", "banana", "cherry"}
y4 = {"google", "microsoft", "apple"}
z4 = x4.symmetric_difference(y4)
print(z4)
