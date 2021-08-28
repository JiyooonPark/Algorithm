# my solution
def solution_my(n, k, arr_a, arr_b):
    sorted_a = sorted(arr_a)
    sorted_b = sorted(arr_b, reverse=True)
    print("A: ", sorted_a)
    print("B: ", sorted_b)
    for i in range(k):
        if sorted_a[i] < sorted_b[i]:
            sorted_a[i], sorted_b[i] =  sorted_b[i], sorted_a[i]
        else:
            break
    print("A: ", sorted_a)
    print("B: ", sorted_b)
    return sum(sorted_a)

# given solution
def solution_given():
    pass

def generate_inputs():
    import random
    # n = random.randint(1, 100)
    n = 15
    k = random.randint(1, n)
    arr_a = [random.randint(1, 1000) for x in range(n)]
    arr_b = [random.randint(1, 1000) for x in range(n)]
    return n, k, arr_a, arr_b
if __name__ == '__main__':
    max_n = 1000
    n, k, arr_a, arr_b = generate_inputs()
    print('k: ', k)
    print(solution_my(n, k, arr_a, arr_b))