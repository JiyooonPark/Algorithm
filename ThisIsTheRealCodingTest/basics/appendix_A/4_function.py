def add ( a, b):
    return a+b
print(add(3, 41))

c = 0

def cummmulative(i):
    global c
    c += i

for i in range(10):
    cummmulative(i)
print(c)

print( (lambda a, b : a+b)(4, 10))