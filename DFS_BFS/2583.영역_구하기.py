from collections import deque

# 동 남 서 북
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]


def bfs(graph, start):
    queue = deque([start])

    result = 1
    while queue:
        y, x = queue.popleft()
        for dy, dx in dirs:
            xx = x + dx
            yy = y + dy

            if xx < 0 or xx >= N or yy < 0 or yy >= M:
                continue

            if graph[yy][xx] == 0:
                result += 1
                graph[yy][xx] = 1
                queue.append((yy, xx))

    return result


for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] += 1

results = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = 1
            results.append(bfs(graph, (i, j)))

results.sort()
print(len(results))
print(*results)
