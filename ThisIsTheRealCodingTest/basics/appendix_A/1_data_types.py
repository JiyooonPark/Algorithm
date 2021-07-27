# Data types

a = -.7
print(a)
a=10e3
print(a)
a = 1.234212
print( round (a, 2) )

# list initialization

a = [0] * 10
print(a)
a[4] = 10
print(a)

array = [i for i in range(20) if i % 2 == 1 ]
print(array)

# 2D array
array = [[0] * 3 for _ in range(4)]
print(array)
array = [[0] * 4]*3
print(array)
array.append(1)
# .append .sort .reverse .insert .count .remove

a = [i for i in range(10)]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)

# dictionary
d = dict()
d['hello'] = "HEHE"
d['bye'] = "HUH?"
print(d)
d.keys()
d.values()

# set 
s = set(array)
s.add(9)
s.update([2, 3, 4])
s.remove(3)