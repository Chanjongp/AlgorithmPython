import sys
from collections import deque


def bfs(graph, start):
    visited, queue = [False] * (n + 1), deque([start])
    visited[start] = True

    cnt = 1
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1

    return cnt


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[y].append(x)


max_result = 0
results = []
visited = [False] * (n + 1)

for i in range(1, n + 1):
    temp_result = bfs(graph, i)
    if temp_result > max_result:
        max_result = temp_result
        results.clear()
        results.append(i)

    elif temp_result == max_result:
        results.append(i)


print(*results)
