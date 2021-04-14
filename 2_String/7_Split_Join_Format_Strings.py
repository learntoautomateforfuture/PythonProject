"""
Dividing into parts is spliting
Return type of split() is a list
syntax: string.split()
"""
# Default separator to split() is whitespace
abc = "Happy coding in python"
print(abc.split())

# If we want to use other separators , then pass it as argument
date = "05-02-2021"
print(date.split('-'))

"""If we want the given string to be divided into a 
particular no:of elements we can specify using the parameter """
fruits = "apple#orange#berry#pineapple#grapes"
x = fruits.split('#', 2)
print (x)

"""
Join 2 strings using join() method
syntax: String = separator.join(iterable)
iterable can be list,set,tuple or array datatype
"""

list = ['Happy', 'coding', 'in', 'python']
x = "-".join(list)
print (x)

"""
Format Strings: Using this method we can combine
strings & numbers or any datatype

Format () takes the argument, formats them & 
places them in the string where there is placeholders {}.
"""

# Emptied Placeholder
no = 10
age = 28
emptyph = "My num is {} and my age is {}"
print(emptyph.format(no, age))

# Indexed Placeholder
indexedph = "My num is {1} and my age is {0}"
print(indexedph.format(age, no))

# Named Placeholder
namedph = "My num is {n} and my age is {age}"
print(namedph.format(n=40, age=30))
