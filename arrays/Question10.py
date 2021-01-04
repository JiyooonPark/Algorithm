# 2021.01.03
# In-place merge two sorted arrays
# Given two sorted arrays X[] and Y[] of size m, n, merge elements of X[]
# with elements of array Y[] by maintaining the order.
# i.e. fill X[] with first m smallest elements and fill Y[] with remaining elements

# input = [1,4,7,8,10], [2, 3, 9]
# output = [1, 2, 3, 4, 7], [8, 9, 10]


def merge(X, Y):
    x_len = len(X)

    XY = list()
    XY.extend(X)
    XY.extend(Y)
    XY.sort()

    x = list()
    y = list()

    for i in range(x_len):
        x.append(XY[i])
    for i in range(x_len, len(XY)):
        y.append(XY[i])
    return (x,y)


if __name__ == '__main__':
    X = [1, 4, 7, 8, 10]
    Y = [2, 3, 9]

    X, Y = merge(X, Y)

    print("X:", X)
    print("Y:", Y)
