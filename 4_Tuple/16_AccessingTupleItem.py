"""
Tuple items are indexed and you can access them by referring to the index number
"""
tuple3 = ("Apple", "Banana", 89, 4.8, True, 89)
print (tuple3[2])

# Negative Indexing - starts from the end
print (tuple3[-1])

# Range of indexes
print (tuple3[0:2])

# Check if an item is present in the list using ‘in’ keyword
tuple3 = ("Apple", "Banana", 89, 4.8, True, 89)
if "Banana1" in tuple3:
    print ("Found")
else:
    print ("not found")
