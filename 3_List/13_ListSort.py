"""
* sort() method that will sort the list alphanumerically,
ascending, by default
* By default the sort() method is case sensitive,
resulting in all capital letters being sorted before lower case letters
* If the list has both alphabets & numbers,
then it gets sorted in ascending order by taking numbers first & then alphabets

"""
list6 = [79, 3, 89]
list6.sort()
print (list6)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

"""
To sort in descending order, use the keyword argument reverse = True
"""
list6 = [79, 3, 89]
list6.sort(reverse = True)
print (list6)

"""
To sort with case insensitive,
we have a built-in functions as key functions - str.lower
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

"""
To Reverse the order, we have a method called reverse()
which reverses all the items in the list
"""
list7 = ["summer", "winter",  "spring", 79, 3, 89, "Apple", "Cherry"]
print (list7)
list7.reverse()
print (list7)

"""
copy() method is used to copy the items from one list to another list
"""

list8 = ["summer", "winter",  "spring"]
newlist = list8.copy()
print (newlist)

"""
list() method is another way to make a copy
"""
list8 = ["summer", "winter",  "spring"]
newlist8 = list(list8)
print (newlist8)