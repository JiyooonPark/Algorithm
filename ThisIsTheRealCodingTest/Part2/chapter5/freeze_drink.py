# my solution
def solution_my(N, M, board):
    zeros = 0
    for list in board:
        for i in list:
            if i == 0:
                zeros += 1
    B = []
    temp = []
    for i in range(M+2):
        temp.append(3)
    B.append(temp)
    for i in board:
        B.append([3]+i+[3])
    B.append(temp)
    for i in B:
        print(i)

    ice = 0
    count = 0
    stack= []
    for i in range(1, N+1):
        for j in range(1, M+1):
            # print(B[i][j])
            if count >= zeros:
                return ice
            if B[i][j]==0:
                ice += 1
                stack.append([i, j])
                while len(stack)!=0:
                    [I, J] = stack.pop()
                    for k in [[0, 0],[-1, 0], [0, -1], [1, 0], [0, 1]]:
                        if B[I+k[0]][J+k[1]] == 0:
                            stack.append([I + k[0], J + k[1]])
                            B[I + k[0]][J + k[1]] = 2
                            count += 1
            else:
                continue

def dfs(x, y, board, N, M):
    if x<= -1 or x>=N or y<=-1 or y>=M:
        return False
    if board[x][y] == 0:
        board[x][y] = 1
        dfs(x-1, y, board, N, M)
        dfs(x+1, y, board, N, M)
        dfs(x, y-1, board, N, M)
        dfs(x, y+1, board, N, M)
        return True
    return False

# given solution
def solution_given(N, M, board):
    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j, board, N, M)== True:
                result+= 1
    print(result)

def generate_inputs():
    import random
    N = random.randint(1, 10)
    M = random.randint(1, 10)
    N, M = 5, 5
    board = []
    temp = []
    for i in range(N):
        for j in range(M):
            temp.append(random.randint(0, 1))
        board.append(temp)
        temp=[]
    print('=======================')
    for i in board:
        print(i)
    print('=======================')
    return N, M, board
if __name__ == '__main__':
    N, M, board = generate_inputs()

    print(solution_given(N, M, board))