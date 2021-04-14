"""
Break Keyword:
    Terminates the loop when the condition is satisfied.
"""
n = 0
while n <= 10:
    print (n)
    n = n + 1
    if (n == 4):
        break
print(" Break the loop")

""" 
Continue Keyword:
    Used inside a loop to skip the statement in the body 
    of the loop for current iteration & jump to the beginning of the loop 
    for next iteration.
"""
n = 0
while n < 5:
    n = n + 1
    if (n == 4):
        continue
    print (n)

print (" Continue the loop")

for i in range(10, 16):
    if (i == 14):
        continue
    print (i)

"""
Pass Keyword:
     When there is no need to code/ execute, 
     but still requires to make the code syntactically correct.
"""
for i in range(10, 16):
    pass


