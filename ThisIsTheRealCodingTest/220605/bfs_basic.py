from collections import deque
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# queue.append(1)
# queue.popleft()

# mine bfs
visited = [False]*9
def bfs1(n, graph, visited):

    queue = deque()
    queue.append(n)

    while not len(queue) == 0:
        n = queue.popleft()
        print(n,end=' ')

        visited[n]=True
        for i in graph[n]:
            if visited[i] == False and i not in queue:
                queue.append(i)

# bfs1(1, graph, visited)

# book answer
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
bfs(graph, 1, visited)

