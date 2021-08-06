def solution_try1(n, m, k):
    # sort -> get max index -> until maxed out add -> move to next index
    total = 0
    sum = 0
    count = 0
    n.sort()
    while total < m:
        if count < k:
            sum += n[-1]
            count += 1
            # print(n[-1], end='+ ')
        else:
            sum += n[-2]
            count = 0
            # print(n[-2], end='+ ')
        total +=1


    return sum
def solution_sequence(n, m, k):
    n.sort()
    first = n[-1]
    second = n[-2]
    fs = first*k + second
    return fs * (m/(k+1)) + first * (m%(k+1))


def generate_inputs(max_n, max_m, max_k):
    import random
    n = []
    for x in range(random.randint(2, max_n)):
        n.append(random.randint(1, 10000))
    m = random.randint(3, max_m)
    k = random.randint(3, m+1)
    return n, m, k
if __name__ == '__main__':
    list = []
    max_n = 1000
    max_m = 10000
    max_k = 10000
    n, m, k = generate_inputs(max_n, max_m, max_k)
    # n, m, k = generate_inputs(30,10, 10)
    n = [2, 4, 5, 4, 6]
    m = 8
    k = 3
    print("n = {}, m = {}, k = {}".format( n, m, k))
    print(solution_sequence(n, m, k))