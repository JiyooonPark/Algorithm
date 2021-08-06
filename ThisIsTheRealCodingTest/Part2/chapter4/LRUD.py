def solution_my(N, path):
    pose = [1, 1]
    for p in path:
        if p == 'L' and pose[0] > 1:
            pose = [pose[0] -1, pose[1]]
        elif p == 'R' and pose[0] < N:
            pose = [pose[0] + 1, pose[1]]
        elif p == 'U' and pose[1] > 1:
            pose = [pose[0], pose[1] -1]
        elif p =='D' and pose[1] < N:
            pose = [pose[0], pose[1]+ 1]
        else:
            continue
    return pose

def solution_given(n, m, k):
    pass

def generate_inputs():
    import random
    N = random.randint(1, 100)
    P = random.randint(1, N)
    options = ['L', 'R', 'U', 'D']
    path = []
    for i in range(P):
        path.append(options[random.randint(0, 3)])
    return N, path

if __name__ == '__main__':
    N, path = generate_inputs()
    print(N, path)
    path = 'R R R U D D'.split()
    print(path)

    print(solution_my(N, path))