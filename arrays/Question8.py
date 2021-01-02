# 2021.01.02
# Find maximum product of two integers in an array
# given an array of integers, find maximum product of two integers in an array
# input = [-10, -3, 5, 6, -2]
# output = [-10, -3] or [5, 6]

# feedback
# 1. don't overthink the question

# intuitive version
def maxMult(A):
    B = list()
    BB = list()
    R = list()
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            B.append(A[i] * A[j])
            BB.append((A[i],A[j]))
    for i in range(len(B)):
        if B[i] == max(B):
            R.append(BB[i])
    return R


# smarter version? or is it ?
def maxMult2(A):
    neg = [k for k in A if k<0]
    pos = [k for k in A if k>0]
    zero = [True if 0 in A else False]
    neg.sort()
    pos.sort()
    if not pos:
        if len(neg)==1 and zero:
            return (0,)
        else:
            return (neg[0],neg[1])
    else:
        B = list()
        B.append((neg[0],neg[1]))
        B.append((pos[-1],pos[-2]))
        if B[0][0]*B[0][1] == B[1][0]*B[1][1]:
            return B
        else:
            return [B[0] if B[0][0]*B[0][1] > B[1][0]*B[1][1] else B[1]]
# suggested
def maxMult4(A):
    n = len(A)
    A.sort()
    B = list()
    if (A[0] * A[1]) > (A[n - 1] * A[n - 2]):
        B.append((A[0], A[1]))
    elif (A[0] * A[1]) < (A[n - 1] * A[n - 2]):
        B.append((A[n - 1], A[n - 2]))
    else:
        B.append((A[0], A[1]))
        B.append((A[n - 1], A[n - 2]))
    return B
# suggested
def maxmult3(A):
    max_product = float('-inf')
    max_i = max_j = -1

    # consider every pair of elements
    for i in range(len(A) - 1):
        for j in range(i + 1, len(A)):
            # update maximum product if required
            if max_product < A[i] * A[j]:
                max_product = A[i] * A[j]
                (max_i, max_j) = (i, j)

    print("Pair is", (A[max_i], A[max_j]))


if __name__ == '__main__':
    A = [-10, -3, 5, 6, -2]
    # A = [-100, 2, 3, 1, 2321,32,1, 3,2,-22, 1, 200000]
    R = maxMult4(A)
    for i in range(len(R)):
        print(R[i], end=" ")
        if i == len(R)-1:
            continue
        else:
            print("or ",end="")