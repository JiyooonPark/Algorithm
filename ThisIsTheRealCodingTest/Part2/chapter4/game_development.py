# my solution
def solution_my(N,M, B ,pose):
    direction = pose[2]
    count = 0
    visualization_init(N, M, B)
    while True:

        # print('count:', count, 'direction: ', direction)
        if direction == 0:
            next = [0, 1]
        elif direction==1:
            next = [1, 0]
        elif direction==2:
            next = [0, -1]
        else:
            next = [-1, 0]

        #check
        out = False
        for [x, y] in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if B[pose[0]+x][pose[1]+y] == 0:
                out = True
                direction = (direction+1) % 4
                # print('yep')
            else:
                # print('nope')
                continue
        if out == False:
            break

        if 0<pose[0]+ next[0]<N and 0 < pose[1]+ next[1]<M and B[pose[0]+ next[0]][pose[1]+next[1]] == 0:

            pose[0], pose[1] = pose[0]+next[0], pose[1]+next[1]
            B[pose[0]][pose[1]] = 2
            count += 1
            visualization(N,M, B ,pose)
            print('count:', count, 'direction: ', direction)
        else:
            direction = (direction+1)%4

    return count

# given solution
def solution_given(N,M, B, pose):
    pass

def generate_inputs():
    import random
    B= []
    temp = []
    N = random.randint(3, 10)
    M = random.randint(3, 10)
    N, M = 5, 5

    for i in range(M+2):
        temp.append(3)
    B.append(temp)
    temp = []
    for i in range(N):
        temp.append(3)
        for j in range(M):
            temp.append(random.randint(0,1))
        temp.append(3)
        B.append(temp)
        temp = []
    for i in range(M+2):
        temp.append(3)
    B.append(temp)
    temp = []

    pose = [0,0]
    while B[pose[0]][pose[1]] != 0:
        pose = [random.randint(0, N-1), random.randint(0, M-1) , random.randint(0, 3)]
        print('pose: ', pose)

    print('pose: ', pose, N, M)
    return N,M, B, pose
def visualization(N, M, B, pose):
    print('============================')
    for i in range(N+2):
        for j in range(M+2):
            if [i, j]== [pose[0], pose[1]]:
                print("*", end= ' ')
            else:
                print(B[i][j], end=' ')
        print()
def visualization_init(N, M, B):
    print('==========INIT============')
    for i in range(N+2):
        for j in range(M+2):
            print(B[i][j], end=' ')
        print()


if __name__ == '__main__':
    N,M, B, pose = generate_inputs()
    print(solution_my(N,M, B ,pose))
