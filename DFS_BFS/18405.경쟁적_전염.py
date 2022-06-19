from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

# 동 남 서 북
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(graph, start, find_second):
    queue = deque(start)

    while queue:
        x, y, second = queue.popleft()
        if second == find_second:
            return

        virus = graph[x][y]
        for dx, dy in dirs:
            xx = x + dx
            yy = y + dy
            if xx < 0 or xx >= n or yy < 0 or yy >= n:
                continue

            # 전파할 좌표에 바이러스가 있으면
            if graph[xx][yy] > 0:
                continue

            graph[xx][yy] = virus
            queue.append((xx, yy, second + 1))


graph, initial_virus = [], []
for row in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    graph.append(line)
    [initial_virus.append([row, col, 0]) for col, val in enumerate(line) if val > 0]

## 순서 정렬
initial_virus.sort(key=lambda x: graph[x[0]][x[1]])
s, x, y = map(int, sys.stdin.readline().split())

# 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다
bfs(graph, initial_virus, s)
print(graph[x - 1][y - 1])
