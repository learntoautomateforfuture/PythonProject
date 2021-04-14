# remove() method - If the item to remove does not exist, it will throw an error
set1 = {"apple", "banana", "cherry"}
set1.remove("banana")
print(set1)

# discard() method - If the item to remove does not exist, it will not throw an error
set2 = {"apple", "banana", "cherry"}
set2.discard("banana")
print(set2)

# pop() method - This method will remove the last item.
# Return value of the pop() method is the removed item.
set3 = {"apple", "banana", "cherry"}
x = set3.pop()
print(x)
print(set3)

# clear() method - This empties the set
set4 = {"apple", "banana", "cherry"}
set4.clear()
print(set4)

# del keyword - Will delete the set completely
set5 = {"apple", "banana", "cherry"}
del set5
print(set5)
