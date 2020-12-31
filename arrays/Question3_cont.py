# 2020.12.31
# Print all sub-arrays with 0 sum
# subarrays : continuous arrays

# feedback
#   1. in for loop, when using range, +1 or not
#   2. enumerate
def printAllSubLists(arr):

    zero_sum=list()
    for i,v in enumerate(arr):
        for j in range(i,len(arr)+1):
            if (sum(arr[i:j]) == 0) and arr[i:j]:
                zero_sum.append(arr[i:j])
    for i in zero_sum:
        print(i)


if __name__ == '__main__':
    A = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    printAllSubLists(A)