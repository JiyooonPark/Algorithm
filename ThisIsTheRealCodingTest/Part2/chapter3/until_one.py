def solution_my(N, K):
    count = 0
    while N > 1:
        count += 1
        if N % K == 0 :
            N //= K
        else:
            N -= 1
    return count

def solution_given(N, K):
    count = 0
    while N >= K:
        if N % K == 0:
            N //= K
            count += 1
        else:
            temp = N - K * (N // K)
            N -= temp
            count += temp
    while N > 1:
        N -= 1
        count += 1
    return count

def generate_inputs(max_n,max_k):
    import random
    N = random.randint(2, max_n)
    K = random.randint(2, N)
    return N, K
if __name__ == '__main__':
    max_n = 100000
    max_k = 100000
    N,K = generate_inputs(max_n, max_k)
    # print( N, K)

    print(solution_my(N,K))
    # print(solution_given(25, 3))