# 2021.01.02
# Find duplicate element in a limited range array
# given a limited range of array of size n where array contains elements
# between 1 to n-1 with one element repeating, find the duplicate number in it.

# feedback
# 1. algorithms don't always have to be fancy or computer sciency

def findDuplicate(A):
    B = list()
    for i in A:
        if i in B:
            print('the duplicate number is',i)
            return i
        B.append(i)
    return False

def findDuplicate2(A):
    A_sum=sum(A)
    real_sum = 0
    for i in range(min(A), max(A)+1):
        real_sum += i
    print('the duplicate number is',A_sum-real_sum)
    return A_sum-real_sum

if __name__=='__main__':
    A = [1,2,3,4,4]
    findDuplicate2(A)
