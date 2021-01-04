# 2021.01.04
# Find index of 0 to be replaced to get maximum length sequence of continuous ones
inputX = [0,0,1,0,1,1,1,0,1,1]


def findIndexofZero(A):
    c = dict()
    for i in range(len(A)):
        A[i] = 1
        j = i
        count = 0
        while A[j] & A[j] == 1:
            count += 1
            j += 1
        j = i - 1
        while A[j] & A[j] == 1:
            count += 1
            j -= 1
        c[i]= count

    print(c)




if __name__ == '__main__':

    A = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]

    index = findIndexofZero(A)
    if index != -1:
        print("Index to be replaced is", index)
    else:
        print("Invalid input")