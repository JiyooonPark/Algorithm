# my solution
def solution_my(N, M, maze):
    B = []
    temp = []
    for i in range(M+2):
        temp.append(3)
    B.append(temp)
    for i in maze:
        B.append([3]+i+[3])
    B.append(temp)


    pose= [1, 1]
    stack = []
    ways = [[1, 0], [0, -1], [0, 1], [-1, 0]]
    stack.append(pose)
    while pose != [N, M]:
        print('stack:' ,stack)
        for i in B:
            print(i)
        print('===================')
        x, y = stack.pop()
        for [i, j] in ways:
            if B[x+i][ y+j] == 1:
                stack.append([x+i, y+j])
                B[x + i][y + j] = 8

            pose = [x, y]
    count =0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] == 8:
                count += 1
    return count
# given solution
def solution_given():
    pass

def generate_inputs():
    pass
if __name__ == '__main__':
    # N = generate_inputs()
    N = 4
    M = 5
    maze = [
        [1, 0, 0, 0, 1],
        [1, 1, 0, 0, 1],
        [0, 1, 1, 0, 0],
        [1, 1, 1, 1, 1]
    ]
    print(solution_my(N, M, maze))