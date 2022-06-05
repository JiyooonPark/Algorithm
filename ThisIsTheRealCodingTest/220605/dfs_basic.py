'''

can't think of a better way to do it cuz I am hungry :p
'''

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

# mine
visited = [0 for i in range(9)]
def dfs_print(cnode, stack, visited):
    visited[cnode] = 1
    stack.append(cnode)
    # print(f"Stack: {stack}\nVisited: {visited}")

    working_on = stack.pop()
    print(working_on, end=' ')

    for i in graph[working_on]:
        if visited[i] == 0:
            stack.append(i)
            dfs_print(stack.pop(),stack, visited)

    if len(stack)==0:
        return

order = dfs_print(1, [], visited)

# answer
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
visited = [False]*9
dfs(graph, 1, visited)