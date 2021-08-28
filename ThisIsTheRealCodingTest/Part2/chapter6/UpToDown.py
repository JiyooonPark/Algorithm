# my solution
def solution_my(n, arr):

    return sorted(arr, reverse=True)
# given solution
def solution_given():
    pass

def generate_inputs():
    import random
    # n = random.randint(0, 1000)
    n = 20
    arr = [random.randint(0, 1000) for x in range(n)]
    return n, arr
if __name__ == '__main__':

    n, arr = generate_inputs()

    print(solution_my(n, arr))