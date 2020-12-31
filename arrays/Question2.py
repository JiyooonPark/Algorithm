# 2020.12.31

# Check if subarray with 0 sum is exists or not
# input = { 3, 4, -7, 3, 1, -4, -2, -2 }
# Output = Subarray with 0 sum exists
# The sub-arrays with 0 sum are
# {3 , 4, -7}
# {4, -7, 3}
# {-7, 3, 1, 3}

# feedback
#   1. how to find all subsets of all arrays.
#   2. lists in one line
#   3. difference between .extend and .append
#   4. Idea behind finding sum of zero
# mine
def zeroSumSublist(arr):
    zero_arr = list()
    neg_arr = [i for i in arr if i<0]
    pos_arr = [i for i in arr if i>0]
    # print(pos_arr)
    # print(neg_arr)

    for i in powerset(neg_arr):
        for j in powerset(pos_arr):
            if sum(j) == abs(sum(i)):
                zero_temp = list()
                zero_temp.extend(i)
                zero_temp.extend(j)
                zero_arr.append(zero_temp)
    print(zero_arr)
    print(len(zero_arr))
    return zero_arr


def powerset(s):
    x = len(s)
    power_arr = list()
    for i in range(1<<x):
        # print(i)
        temp = [s[j] for j in range(x) if (i & (1<<j))]
        # temp = list(set(temp))
        temp.sort()
        if temp not in power_arr:
            power_arr.append(temp)
    power_arr.sort()
    # print("power set : ", power_arr[1:])
    return power_arr[1:]

# Function to check if sublist with 0 sum is present
# in the given list or not
def zeroSumSublist1(A):
    # create an empty set to store sum of elements of each
    # sublist A[0..i] where 0 <= i < len(A)
    s = set()

    # insert 0 into set to handle the case when sublist with
    # 0 sum starts from index 0
    s.add(0)

    sum = 0

    # traverse the given list
    for i in A:

        # sum of elements so far
        sum += i

        # if sum is seen before, we have found a sublist with 0 sum
        if sum in s:
            return True

        # insert sum so far into set
        s.add(sum)

    # we reach here when no sublist with 0 sum exists
    return False


if __name__ == '__main__':

    A = [4, -6, 3, -1, 4, 2, 7]
    A= [ 3, 4, -7, 3, 1, -4, -2, -2]
    A = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

    if zeroSumSublist(A):
        print("Sublist exists")
    else:
        print("Sublist do not exist")