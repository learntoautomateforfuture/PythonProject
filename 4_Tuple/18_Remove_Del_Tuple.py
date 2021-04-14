"""
remove() method  - Tuple items can be removed by converting it to a list,
remove it & then convert back to tuple
"""
tuple3 = ("Apple", "Banana", "Cherry", "kiwi")
li = list(tuple3)
li.remove("Banana")
tuple3 = tuple(li)
print (tuple3)


# Del keyword - delete the tuple completely
#del tuple3
#print (tuple3)