# 2020.12.30
# Find pair with given sum in an array

# Input:
#     arr = [8, 7, 2, 5, 3, 1]
#     sum = 10
#
# Output:
# Pair found at index 0 and 2 (8 + 2)
# or
# Pair found at index 1 and 4 (7 + 3)

# mine
arr = input('input the array: ')
arr = arr.split(',')
iarr=[]
for i in arr:
    iarr.append(int(i))
target = int(input ('number you want to find: '))
print('trying to find %d in ' % target, iarr)

iarr.sort()
if target > iarr[-1]+iarr[-2]:
    print("none found")
else:
    index = 0
    for i in iarr[:int(len(iarr)/2)]:
        if target-i in iarr[index:]:
            print('Pair found at index %d and %d (%d + %d)' % (index, iarr.index(target-i), i, target-i))
        index= index+1


# naive
# Naive method to find a pair in a list with the given sum
def findPair(A, sum):
    # consider each element except the last
    for i in range(len(A) - 1):

        # start from the i'th element till the last element
        for j in range(i + 1, len(A)):

            # if the desired sum is found, print it and return
            if A[i] + A[j] == sum:
                print("Pair found at index", i, "and", j)
                return

    # No pair with the given sum exists in the list
    print("Pair not found")


# Function to find a pair in an array with a given sum using sorting
def findPair(A, sum):
    # sort the list in ascending order
    A.sort()

    # maintain two indices pointing to end-points of the list
    (low, high) = (0, len(A) - 1)

    # reduce the search space `A[low…high]` at each iteration of the loop

    # loop till search space is exhausted
    while low < high:

        if A[low] + A[high] == sum:  # sum found
            print("Pair found")
            return

        # increment `low` index if the total is less than the desired sum;
        # decrement `high` index if the total is more than the desired sum
        if A[low] + A[high] < sum:
            low = low + 1
        else:
            high = high - 1

    # No pair with the given sum exists
    print("Pair not found")


# Function to find a pair in an array with a given sum using hashing
def findPair(A, sum):
    # create an empty dictionary
    dict = {}

    # do for each element
    for i, e in enumerate(A):

        # check if pair (e, sum-e) exists

        # if the difference is seen before, print the pair
        if sum - e in dict:
            print("Pair found at index", dict.get(sum - e), "and", i)
            return

        # store index of the current element in the dictionary
        dict[e] = i

    # No pair with the given sum exists in the list
    print("Pair not found")
