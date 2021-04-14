""" Write a Program to get a string made of the first 2 & last 2 characters
 from a given string. If the length is less than 2, return instead of empty string
Sample String: pythonprogram , Expected String: pyam
Sample String: py, Expected String : pypy
Sample String: p, Expected String : Empty String """

inputstring = input("Enter the string:")
expectedstring = inputstring[0:2] + inputstring[-2::]
if len(expectedstring) <= 2 :
    print " "
else:
    print expectedstring

""" Write a program to add ing at the end of the given string, 
if it already ends with ing then add ly instead.
Sample String: abc , Expected String: arcing
Sample String: string , Expected String: stringly """

samplestring = input("Enter the string:")
if samplestring.endswith("ing"):
    print(samplestring+'ly')
else:
    print(samplestring + 'ing')