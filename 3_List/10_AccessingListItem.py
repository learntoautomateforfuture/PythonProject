"""
List items are indexed and you can access them by referring to the index number
"""
list1 = ['apple', 89, False, 89.1]

print (list1[0])

# Negative Indexing - starts from the end
print (list1[-1])

# Range of indexes
print (list1[1:3])

# Check if an item is present in the list using in keyword
list2 = ["Apple", "Banana", "Cherry", "Apple1"]
if "Cherry" in list2:
    print ("Found")
