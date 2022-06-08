# ==========================NOTEPAD============================
'''
2022/06/06
START: 14:08    END: 14:23

CHAPTER 5: DFS/BFS

IDEAS:
    ::DFS::
    - pass distance to every recursion

NOTE:
    ::BFS::
    - Better to use bfs instead of dfs
    - bfs uses less space(mem)
    - book answer not fully understood
'''

# ===================MY SOLUTION FUNCTION======================
def dfs(x, y, travel, graph, min_dist):

    if 0<=x<len(graph) and 0<=y<len(graph[0]):

        if [x, y] == [goalx-1, goaly-1]:
            min_dist.append(travel)

        if graph[x][y] == 1:
            graph[x][y] = 2
            dfs(x+1, y, travel+1, graph, min_dist)
            dfs(x-1, y, travel+1, graph, min_dist)
            dfs(x, y+1, travel+1, graph, min_dist)
            dfs(x, y-1, travel+1, graph, min_dist)
            return True
    return False

# ====================SOLUTION FUNCTION========================
from collections import deque

def bfs(x,y, n, m, graph):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for (i,j) in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            if 0<=x+i<n and 0<=y+j<m:
                if graph[x+i][y+j] == 1:
                    queue.append((x+i, y+j))
                    graph[x+i][y+j] = graph[x][y]+1

        print_graph(graph)



# ======================BASIC FUNCTIONS========================

def print_graph(graph):
    print("GRAPH=================")
    for i in graph:
        print(i)

# ========================TEST CASES===========================
graph = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 1, 1]
]
goalx, goaly = 3, 3

graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
goalx, goaly = 5, 6

# ============================MAIN=============================

if __name__ == "__main__":
    min_dist = []
    # dfs(0, 0, 1, graph, min_dist)
    bfs(0,0, 5, 6, graph)
    # print(min(min_dist))