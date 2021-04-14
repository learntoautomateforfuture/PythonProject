# To insert an item at specified index, use insert() method
list6 = ["summer", "winter",  "spring"]
list6.insert(1, "Fall")
print (list6)

# To add an item at the end of the list, use append() method
list7 = ["summer", "winter",  "spring"]
list7.append("Fall")
print (list7)

# To append elements from another list to the current list, use the extend() method
list1 = ["summer", "winter",  "spring"]
list2 = ["car", "bike",  "train"]
list1.extend(list2)
print (list1)