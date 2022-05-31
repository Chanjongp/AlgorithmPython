from collections import deque

t = int(input())
results = []

# 동 남 서 북 (x, y)
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(graph, visited, start, result, max_size):
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        # 2 0
        x, y = queue.popleft()
        for dx, dy in directions:
            xx = x + dx
            yy = y + dy

            # x가 0, y가 0일 경우
            if xx < 0 or yy < 0:
                continue
            # x가 n, y가 m 이상일 경우
            elif xx > max_size[0] or yy > max_size[1]:
                continue

            # 인접 노드가 1일 경우 큐에 추가 및 방문처리
            if graph[xx][yy] == 1 and not visited[xx][yy]:
                queue.append((xx, yy))
                visited[xx][yy] = True


for _ in range(t):
    # 가로 세로 (y, x)
    m, n, k = map(int, input().split())
    # (3, 5)
    max_size = (n - 1, m - 1)
    graph = [[0] * m for _ in range(n)]

    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        ym, xn = map(int, input().split())
        graph[xn][ym] = 1

    # 시작
    result = 0
    for i in range(n):
        for j in range(m):
            # 방문안한 1이면 BFS
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(graph, visited, (i, j), result, max_size)
                result += 1

    results.append(result)

[print(r) for r in results]
