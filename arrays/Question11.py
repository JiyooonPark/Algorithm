# 2021.01.04
# Merge two arrays by satisfying given constraints
# given two sorted arrays X, Y of size m, n where m >= n and X has exactly n vacant cells,
# merge elements of Y in their correct position in array X
# i.e. merge (X,Y) by keeping the sorted order
inputX = [0,2,0,3,0,5,6,0,0]
inputY = [1,8,9,10,15]
output = [1,2,3,5,6,8,9,10,15]

# feedback
# in python.. the questions become so simple..

def merge(X, Y):
    XY = [i for i in X if i != 0]
    XY.extend([i for i in Y if i != 0])
    XY.sort()
    # print(XY)
    return XY

if __name__ == "__main__":
    X = [0, 2, 0, 3, 0, 5, 6, 0, 0]
    Y = [1, 8, 9, 10, 15]
    XY = merge(X, Y)
    print(XY)