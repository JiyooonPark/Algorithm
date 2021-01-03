# 2021. 01. 03
# Sort an array of 0’s, 1’s and 2’s (Dutch National Flag Problem)
# Given an array containing only 0's and 1's and 2's, sort the array
# in linear time and using constant space

# input = [0,1,2,2,1,0,0,2,0,1,1,1,0]
# output = [0,0,0,0,0,1,1,1,1,2,2,2]

# feedback
# 1. three way partition, four way partition?, nth way partition

# mine
def sortLinear(A):
    o = z = t = 0
    for i in A:
        if i == 0:
            z += 1
        elif i == 1 :
            o += 1
        else:
            t += 1
    B = list()
    for i in range(z):
        B.append(0)
    for i in range(o):
        B.append(1)
    for i in range(t):
        B.append(2)
    return B

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# answer
def threeWayPartition(A, end):
    start = mid = 0
    pivot = 1

    while mid <= end:
        if A[mid] < pivot:
            swap(A, start, mid)
            start += 1
            mid += 1
        elif A[mid] > pivot:
            swap(A, mid, end)
            end -= 1
        else:
            mid += 1



if __name__=='__main__':
    A = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 1, 0]
    B = sortLinear(A)
    print(B)
    threeWayPartition(A, len(A)-1)
    print(A)