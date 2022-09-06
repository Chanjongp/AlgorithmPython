from collections import deque
import sys

N = int(input())
graph = [list(sys.stdin.readline()) for _ in range(N)]
visited = [[-1] * (N) for _ in range(N)]

# 동 남 서 북 (x, y)
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(graph, start, visited):
    queue = deque([start])
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        # 끝방까지 가면 리턴
        if x == (N - 1) and y == (N - 1):
            return visited[x][y]

        for dx, dy in dirs:
            xx = x + dx
            yy = y + dy
            if xx < 0 or xx >= N or yy < 0 or yy >= N:
                continue

            # 방문 안했으면
            if visited[xx][yy] == -1:
                # 흰 방일 경우, 흰방부터 탐색하도록 함
                # 탐색하고,
                if graph[xx][yy] == "1":
                    queue.appendleft((xx, yy))
                    visited[xx][yy] = visited[x][y]
                else:
                    queue.append((xx, yy))
                    visited[xx][yy] = visited[x][y] + 1


print(bfs(graph, (0, 0), visited))
