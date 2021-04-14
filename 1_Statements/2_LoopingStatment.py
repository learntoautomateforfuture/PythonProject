# While Loop
x = 0
while (x <= 5):
    print (x)
    x = x + 1

# For Loop
for i in range(10, 15):
    print(i)

# Nested For Loop
for x in range(3):
    print(x)
    for y in range(10, 13):
        print (y)

# Nested While Loop
i, j = 1, 5
while i < 4:
    while j < 8:
        print(i, " ", j)
        j = j + 1
        i = i + 1

# While loop with else block
n = 10
while n > 6:
    print (n)
    n = n - 1
else:
    print ("loop is done")



