from collections import deque


def dfs(graph, start, visited):
    visited[start] = True

    graph[start].sort()
    print(start, end=" ")
    for i in graph[start]:
        if not visited[i] == True:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, start = map(int, input().split())

graph = [[] * (n) for _ in range(n + 1)]
visited1 = [False] * (n + 1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

dfs(graph, start, visited1.copy())
print("")
bfs(graph, start, visited1.copy())
