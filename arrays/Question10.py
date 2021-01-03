# 2021.01.03
# In-place merge two sorted arrays
# Given two sorted arrays X[] and Y[] of size m, n, merge elements of X[]
# with elements of array Y[] by maintaining the order.
# i.e. fill X[] with first m smallest elements and fill Y[] with remaining elements

# input = [1,4,7,8,10]
# output = [2, 3, 9]


def merge(X, Y):
    x_len = len(X)
    y_len = len(Y)

    XY = list()
    XY.extend(X)
    XY.extend(Y)
    print(XY)
    XY.sort()
    print(XY)
    X = Y = []
    for i in range(x_len):
        X.append(XY[i])
    for i in range(y_len):
        Y.append(XY[i])


if __name__ == '__main__':
    X = [1, 4, 7, 8, 10]
    Y = [2, 3, 9]

    merge(X, Y)

    print("X:", X)
    print("Y:", Y)
