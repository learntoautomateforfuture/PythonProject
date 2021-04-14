# Remove() - removes the specified item
list6 = ["summer", "winter",  "spring"]
list6.remove("winter")
print (list6)

# pop() - removes the specified index
list6 = ["summer", "winter",  "spring"]
list6.pop(0)
print (list6)

# If you do not specify the index, the pop() method removes the last item.
list6.pop()
print (list6)

# clear() - empties the list, the list remains but has no content
#list6.clear()
#print list6

# del keyword: deletes the list completely
list5 = ["car", "bike",  "train"]
del list5[0]
print (list5)
del list5
#print list5