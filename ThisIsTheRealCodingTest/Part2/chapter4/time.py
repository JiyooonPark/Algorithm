def solution_my(N):
    # 00:00:00 - N:59:59
    if N < 3:
        threes = 0
    elif N < 13:
        threes = 1
    elif N < 23:
        threes = 2
    else:
        threes = 3

    count  = (N + 1) * 60 * 60 - (N - threes + 1) * 45 * 45
    return count

def solution_given(N):
    count = 0
    for i in range(N+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    return count
def generate_inputs(max_n):
    import random
    N = random.randint(0, max_n)
    return N
if __name__ == '__main__':
    max_n = 23
    N= generate_inputs(max_n)
    N = 5
    print(N)
    print(solution_given(N))