# For loop
tuple4 = ("summer", "winter",  "spring")
for x in tuple4:
    print (x)

# Loop Through the Index Numbers - loop through the tuple items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
tuple4 = ("summer", "winter",  "spring")
for x in range(len(tuple4)):
    print (str(x) +":"+ tuple4[x])

# While loop
"""
Use the len() function to determine the length of the tuple, 
then start at 0 and loop your way through the tuple items by referring to their indexes.
increase the index by 1 after each iteration.
"""
tuple5 = ("summer", "winter",  "spring")
i = 0
while i < len(tuple5):
    print (tuple5[i])
    i = i + 1