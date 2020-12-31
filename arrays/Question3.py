# 2020.12.31
# Print all sub-arrays with 0 sum

# feedback
#   1. read the questions
#   2. powerset ( is there a simpler way to find them?)

def printAllSubLists(arr):

    zero_arr=list()
    for i in powerset(arr):
        if sum(i) == 0:
            zero_arr.append(i)
    zero_arr.sort()
    for i in zero_arr:
        print(i)
    # print(zero_arr)
    print(len(zero_arr))

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


if __name__ == '__main__':
    A = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    printAllSubLists(A)