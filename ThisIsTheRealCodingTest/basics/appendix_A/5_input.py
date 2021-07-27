n = int(input('input a number'))

data = list(map(int, input().split()))
print(data)
data.sort(reverse=True)
print(data)

n, m, k = map(int, input().split())
print(m)

# faster input 
import sys
data = sys.stdin.readline().rsplit()
print(data)

# cannot use str + int + str 
print('hello the number is', 8, ' okay?')

# print sentence
answer = 10
print(f'answer {answer}.')
print('hello {} my name is {}'.format(4, 'suzy'))
print('hello {a} my name is {b}'.format(b = 4, a = 'suzy'))