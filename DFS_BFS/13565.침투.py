import sys
from collections import deque

N, M = map(int, input().split())

# 동 남 서 북
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(graph, start):
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        if x == (N - 1):
            return True

        for dx, dy in dirs:
            xx = x + dx
            yy = y + dy

            if xx < 0 or xx >= N or yy < 0 or yy >= M:
                continue

            if graph[xx][yy] == "0":
                queue.append((xx, yy))
                graph[xx][yy] = "1"

    return False


graph = []
outer_point = []

# Intialize
for _ in range(N):
    data = list(sys.stdin.readline().rstrip())
    graph.append(data)

# 바깥쪽 전류좌표 추가
[outer_point.append([0, index]) for index, i in enumerate(graph[0]) if i == "0"]

result = "NO"
for pos in outer_point:
    if bfs(graph, pos):
        result = "YES"
        break

print(result)
