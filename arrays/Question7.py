# 2021.01.02
# Find maximum length sub-array having equal number of 0’s and 1’s
# given a binary array containing 0 and 1, find maximum length sub-array having
# equal number of 0s and 1s
# input = [0,0,1,0,1,0,0]
# output = [0,1,0,1] or [1,0,1,0]

# feedback
# 1. print(i , end=" ")
# 2. is there a better way to find the index of max list within list?

def equalNum(A):
    B = list()
    BB= list()
    o=z=0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            temp = A[i:j]
            z = [k for k in temp if k==0]
            o = [k for k in temp if k==1]
            if len(z)==len(o):
                B.append(temp)
    # print(B)
    B_len = [len(k) for k in B]
    for i in range(len(B_len)):
        if B_len[i] == max(B_len):
            BB.append(B[i])
    # print(BB)
    return BB


if __name__=="__main__":
    A = [0,0,1,0,1,0,0]
    BB = equalNum(A)
    for i in BB:
        print(i , end=" ")
        if i is BB[-1]:
            continue
        else:
            print('or', end=" ")
