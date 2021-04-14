"""
Boolean DataType:
 Represents a truth value of an expression.
 Value is either True or False
 T & F should be in uppercase
"""
a = True
print (a)
print (type(a))

print((True + True))
print((True - False))

if(True):
    print ("HI")
else:
    print ("ABC")

"""
String DataType:
    Sequence of characters is called as String 
    Surrounded by either single / double quotes
"""
ch = 'a'
print (ch)

"""
Ways to access String Character
* Index
    - Used to access a specific character at the given index of the string
    - syntax: stringvariable[index]
    - Indexing supports both positive & negative indexing 
    - Forward direction index starts from 0 from the beginning of the string
    - Backward direction index starts from -1 from end of the string
    
* Slice
    - To print part of the string
    - syntax: stringvariable[begin:end:step]
    * begin: start of the index
    * end: end of the index
    *step: determines the increment between each index for slicing.
           Can either be +ve or -ve
           if +ve, consider from begin to end-1 in forward direction
           if -ve, consider from begin to end+1 in backward direction     
"""
var = "HelloPython"
print (var)
print (var[5])
#print (var[50])
print (var[-2])

xyz = "HelloApple"
print(xyz[1:5:1])
print(xyz[1:5:2])
print(xyz[-1:-5:-1])
print(xyz[::-1])

"""
Concatenation Operator (+):
    - To join two strings 
"""
X = "Hi" + "Miss"
print (X)

Y = "Hi" + 10
print (Y)

"""
Repetition Operator (*):
    - To write a text multiple times
    - syntax: stringvariable * int
"""
Z = "Help!" * 3
print (Z)

#str() function - To join string argument with another datatype argument
X = "Hi" + str(10.89)
print (X)








