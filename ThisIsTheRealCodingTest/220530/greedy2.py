def solution1(N, M, N_list):
    min_num = 0

    for i in range(N):
        temp = min(N_list[i][:])
        if temp > min_num:
            min_num = temp
    print(min_num)

solution1(3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]])
solution1(2, 4, [[7,3,1,8],[3,3,3,4]])



