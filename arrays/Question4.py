# Sort Binary array in Linear Time
# Given a binary array sort it in linear time and constant space.
# Output should print contain all zeros followed by all ones

# input = {1,0,1,0,1,0,0,1}
# output = {0, 0, 0, 0, 1, 1, 1, 1}

# feedback
# 1. linear time?

def toLinear(A):
    z = 0
    o = 0
    for i in A:
        if i==0:
            o = o+1
        else:
            z = z+1
    B = list()
    for i in range(z):
        B.append(0)
    for i in range(o):
        B.append(1)

    return B

def toLinear2(A):
    B = list()
    for i in A:
        if i == 0:
            B.append(0)
    for i in range(len(A) - len(B)):
        B.append(1)

    return B



if __name__ == '__main__':
    A = [1,0,1,0,1,0,0,1]
    print(toLinear(A))
    print(toLinear2(A))