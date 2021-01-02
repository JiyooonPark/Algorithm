# 2021.01.02
# Find maximum length sub-array having given sum
# given an array of integers, find maximum length sub-array having given sum

# input = [5, 6, -5, 5, 3, 5, 3, -2, 0] sum=8
# output = [-5, 5, 3, 5]

# feedback
# 1. I feel like there may be a better way to solve this question

def sumSub(A,s):
    B = list()
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            temp = A[i:j]
            if sum(temp)==s:
                B.append(temp)
    # print(B)
    B_len=list()
    for i in B:
        # print(i)
        B_len.append(len(i))
    # print(B_len)
    b = [1,2,3,4]
    # print(B_len.index(max(B_len)))
    print("The longest subarray is", B[B_len.index(max(B_len))] , "having length",max(B_len))




if __name__=='__main__':
    A = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    sumSub(A,8)