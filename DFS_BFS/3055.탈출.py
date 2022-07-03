from collections import deque

"""
* : 물
. : 비어있음
X : 돌
S : 고슴도치 위치
D : 비버의 굴

# 탐색 조건
1. 한턴마다 동서남북으로 물 채워짐
2. 고슴도치 이동함
3. 이동 시 인접구간에 물 있으면 못이동
"""

# x, y
R, C = map(int, input().split())

# 북 남 동 서
dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
distance = [[0] * C for _ in range(R)]

WATER = 0
GOSUM = 1


def bfs(graph, start):
    queue = deque(start)
    while queue:
        x, y, distance = queue.popleft()

        for dx, dy in dirs:
            xx = x + dx
            yy = y + dy

            if xx < 0 or xx >= R or yy < 0 or yy >= C:
                continue

            elif graph[x][y] == "X":
                continue

            # S일 때
            if graph[x][y] == "S" and graph[xx][yy] in [".", "D"]:
                if graph[xx][yy] == "D":
                    return distance + 1

                graph[xx][yy] = "S"
                queue.append((xx, yy, distance + 1))

            # *(물)일 때
            elif graph[x][y] == "*" and graph[xx][yy] in [".", "S"]:
                graph[xx][yy] = "*"
                queue.append((xx, yy, 0))

    return "KAKTUS"


#### Initialize
graph = []
start_arr = []

for i in range(R):
    temp = list(input().rstrip())

    for index, v in enumerate(temp):
        if v == "S":
            start = (i, index, 0)
        elif v == "*":
            start_arr.append((i, index, 0))

    graph.append(temp)

start_arr.insert(0, start)

result = bfs(graph, start_arr)
print(result)
