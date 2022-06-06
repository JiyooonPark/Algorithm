'''
start: 13:37
end: 13:54

use bfs with matrix representation of graph.
## for the book answer, why have to return the values in that manner? 
'''

def print_tray(tray):
    print("Tray=================")
    for i in tray:
        print(i)

def bfs(x, y, tray):
    stack = [[x,y]]
    while stack:
        pose = stack.pop()
        # print("POPPED:", pose)
        for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0<=pose[0]+i<len(tray) and 0<=pose[1]+j<len(tray[0]):
                if tray[pose[0]+i][pose[1]+j] == 0:
                    tray[pose[0]+i][pose[1]+j] = 2
                    stack.append([pose[0]+i,pose[1]+j])
    print_tray(tray)
    return tray


def solution1(n, m, tray):
    ice_cubes = 0
    for i in range(n):
        for j in range(m):
            if tray[i][j] == 0:
                tray = bfs(i, j, tray)
                ice_cubes+=1
            else:
                continue
    print("TOTAL ICE:",ice_cubes)

tray = [
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
tray = [
    [0,0,0,1,1,1,0,0],
    [0,0,0,1,1,1,0,0],
    [0,1,1,1,0,1,1,0],
    [1,0,0,1,1,1,0,1],
    [0,0,0,1,0,1,0,0],

]
# bfs(0,0,tray)
# solution1(len(tray), len(tray[0]),tray)

# answer
n, m = len(tray), len(tray[0])

def dfs(x, y):
    if 0<=x<n and 0<=y<m:
        if tray[x][y] == 0:
            tray[x][y] = 2
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x, y-1)
            return False
    return True
ice = 0
for i in range(n):
    for j in range(m):
        if not dfs(i,j):
            ice += 1
print(ice)