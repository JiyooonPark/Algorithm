# internal libraries

result = sum([i for i in range(10)])
print(result)

result = min([i for i in range(10, 1, -1)])
print(result)

result = eval(" (9 + 10) ** 2") # evaluates string 
print(result)

result = sorted([i for i in range(10, 1, -2)], reverse=False)
print(result)

result = sorted([('a', 34), ('b', 10), ('c', 60)], key = lambda x : x[1], reverse=True)
print(result)


# itertools 
from itertools import permutations, product
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

from itertools import combinations
result = list(combinations(data, 2))
print(result)

result = list(product(data, repeat =  2))
print(result)

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)

import heapq

def heapsort(iterable):
    h = []
    result = [] 
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
print(heapsort([4,3,2,432,4,32,14,32143,2,3]))


# bisect
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
print(bisect_right(a, x))

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
print(count_by_range(a, 4, 4))
print(count_by_range(a, -1, 3))

#deque
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)