import sys
from collections import deque

# 행, 열
R, C = map(int, input().split())
SHEEP = 0
WOLF = 1
# 동 남 서 북
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    sheep, wolf = 0, 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            xx = x + dx
            yy = y + dy
            if xx < 0 < R or yy < 0 < C:
                continue

            elif visited[xx][yy] or graph[xx][yy] == "#":
                continue

            if graph[xx][yy] == "o":
                sheep += 1
            elif graph[xx][yy] == "v":
                wolf += 1

            visited[xx][yy] = True
            queue.append((xx, yy))

    return [sheep, 0] if sheep > wolf else [0, wolf]


graph = []
wolfs = []
visited = [[False] * C for _ in range(R)]
result = [0, 0]
sheep = 0

for i in range(R):
    data = list(sys.stdin.readline().rstrip())
    # 늑대 위치 초기화
    for index, val in enumerate(data):
        if val == "v":
            wolfs.append((i, index))
        elif val == "o":
            sheep += 1

    graph.append(data)

# 늑대가 없으면 양만 출력
if not wolfs:
    print(sheep, 0)
    exit(0)

for wolf in wolfs:
    if not visited[wolf[0]][wolf[1]]:
        temp = bfs(graph, visited, wolf)
        result[SHEEP] += temp[SHEEP]
        result[WOLF] += temp[WOLF]

print(*result)
