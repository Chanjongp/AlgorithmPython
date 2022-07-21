"""
6 5
1 2
2 5
5 1
3 4
4 6
"""
from collections import deque

N, M = map(int, input().split())

graph = [[] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)


def bfs(start):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# Initialize
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


result = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        result += 1

print(result)
