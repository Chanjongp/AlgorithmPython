from collections import deque


def dfs(graph, v, visited):
    visited[v] = True

    print(v, end=" ")
    for i in graph[v]:
        if not visited[i] == True:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        value = queue.popleft()
        print(value, end=" ")
        for i in graph[value]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n + 1)]
visited1 = [False] * len(graph)
visited2 = [False] * len(graph)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for i in range(m):
    graph[i].sort()


dfs(graph, v, visited1)
print("")
bfs(graph, v, visited2)
