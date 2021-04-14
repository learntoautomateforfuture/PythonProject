# For loop
list1 = ["summer", "winter",  "spring"]
for x in list1:
    print (x)

# Loop Through the Index Numbers - loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
list1 = ["summer", "winter",  "spring"]
for x in range(len(list1)):
    print ((str(x) + list1[x]))

# While loop
"""
Use the len() function to determine the length of the list, 
then start at 0 and loop your way through the list items by refering to their indexes.
increase the index by 1 after each iteration.
"""
list1 = ["summer", "winter",  "spring"]
i = 0
while i < len(list1):
    print (list1[i])
    i = i + 1