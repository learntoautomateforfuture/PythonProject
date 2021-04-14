"""
Global:
    Variables declared outside the function are global variables
    Scope of it is through out the program

Local:
    Variables declared inside the function are local variables
    Scope of it is within the function
    Cannot be accessed outside the function

Function:
    Set of statements bounded in a particular area
    def localFunc(): -> Function defintion
    localFunc() -> Calling function

Global Keyword:
    If w want to use local variable outside a function then
     we have to make it as global using 'global' keyword
"""

x = 40  # Global Variable
def localFunc():
    y = 30 # Local Variable
    print ("y is local", y)
localFunc()
print ("x is global", x)


def localFunc():
    global x
    x = 50
    print ("Value of x inside localFunc:", x)
localFunc()
print ("Value of x outside localFunc:", x)

