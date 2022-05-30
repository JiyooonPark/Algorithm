
def solution1(N, M, K, N_list):
    if K > M:
        raise "invalid input"
    N_list.sort()

    same = 0
    sum_ = 0
    for i in range(M):
        if same >= K:
            sum_ += N_list[-2]
            same = 0
        else:
            same +=1
            sum_ += N_list[-1]
    print(sum_)

def solution2(N, M, K, N_list):
    if K > M:
        raise "invalid input"
    N_list.sort()

    first = N_list[-1]
    second = N_list[-2]

    sum = (first*K+second)*(M//(K+1))+first*(M%(K+1))
    print(sum)

solution2(5, 8, 3, [2, 4, 5, 4, 6])


