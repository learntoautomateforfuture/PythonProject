"""
SubString : Sequence of characters
To check if a substring or a character is present in string or not
use membership operators : in & not
"""
mainString = "Python is a Programming Language"
substring = 'P' in mainString
print (substring)

substring = 'P' not in mainString
print (substring)

string1 = input("Enter the main String:")
substring1 = input("Enter the substring:")
if substring1 in string1:
    print ("Its Found")
else:
    print ("Not Found")
#####################################################
"""
Python compares two strings by comparing each
 character based on their unicode values
"""
print(ord('A'))
print(ord('$'))

print(ord('p'))
print(ord('t'))

str1 = "Happy"
str2 = "Hat"
if str1 == str2:
    print ("Both are equal")
elif str1 < str2:
    print ("str1 is less than str2")
else:
    print ("str2 is greater than str1")
##################### String Methods ################################
"""
Remove spaces in string :
lstrip(), rstrip(), strip()
"""
city = " Bangalore "
print (city.rstrip())
print (city.lstrip())
print (city.strip())

"""
To Find index of a given string:
find(substr), rfind(substr), index(substr), rindex(substr)
"""
city = "BangaloreBBAABAAB"
print (city.find('a'))
print (city.rfind('A'))
print (city.index('g'))
print (city.rindex('A'))

"""
count(substr) - To count the no:of times a specific character/substring present in a given string
replace(oldstring, newstring) - To replace the string with another string
"""
city = "BangaloreManagalore"
print(city.count('galo'))
print(city.replace('B','M'))

"""
To check the start & end part of the string:
startswith(substr), endswith(substr)
"""
s =" This is a python program"
print (s.startswith("Thi"))
print (s.endswith("am"))


