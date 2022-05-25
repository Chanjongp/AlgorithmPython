from collections import deque

############ BFS
def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True
    result = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result += 1

    return result


n = int(input())
m = int(input())

graph = [[] * n for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


result = bfs(graph, 1, visited)
print(result)


############ DFS
result = 0


def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i] == True:
            global result
            result += 1
            dfs(graph, i, visited)


n = int(input())
m = int(input())

graph = [[] * n for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


dfs(graph, 1, visited)
print(result)
