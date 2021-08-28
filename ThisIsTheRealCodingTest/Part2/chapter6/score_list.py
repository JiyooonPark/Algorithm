# my solution
def solution_my(n, arr):
    result = sorted(arr, key=setting, reverse=True)
    return result
def setting(data):
    return data[1]
# given solution
def solution_given():
    pass

def generate_inputs():
    import random
    # import random_word
    # n = random.randint(0, 1000)
    n = 20
    arr = [random.randint(0, 1000) for x in range(n)]
    name = [random.randint(1000, 2000) for x in range(n)]
    return n, zip(name, arr)
if __name__ == '__main__':
    max_n = 1000
    n, arr = generate_inputs()

    print(solution_my(n, arr))