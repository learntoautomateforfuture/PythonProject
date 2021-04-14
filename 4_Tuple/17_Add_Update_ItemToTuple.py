"""
append() - convert it to a list, update it & then convert back to tuple
Adds item at the end of the list/tuple
"""
tuple1 = ("Apple", "Banana", "Cherry", "kiwi")
add = list(tuple1)
add.append("melon")
tuple1 = tuple(add)
print (tuple1)


"""
Change the item using index value:  
convert it to a list, update it & then convert back to tuple
"""
tuple2 = ("Apple", "Banana", "Cherry", "kiwi")
print (tuple2)
update = list(tuple2)
update[3] = "Dog"
tuple2 = tuple(update)
print (tuple2)
