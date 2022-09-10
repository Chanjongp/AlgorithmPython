# https://www.acmicpc.net/problem/18405
"""
X, Y -> S초가 지난 후에

N X N
1 ~ K 바이러스 종류

(0, 0) -> 1
(0, 2) -> 2
(2, 0) -> 3

바이러스 존재 X -> 0 출력

3 3
1 0 2
0 0 0
3 0 0
2 3 2

2초 뒤 (3 ,2) 출력
S, X, Y

매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 
또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.
"""

from collections import deque

# 동 남 서 북
dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(graph, virus_pos, find_second):
    queue = deque(virus_pos)

    while queue:
        x, y, second = queue.popleft()
        if second == find_second:
            return

        for dx, dy in dirs:
            xx = x + dx
            yy = y + dy

            if xx < 0 or xx >= N or yy < 0 or yy >= N:
                continue

            # 먼저 감염되었으면
            if graph[xx][yy] > 0:
                continue

            graph[xx][yy] = graph[x][y]
            queue.append((xx, yy, second + 1))


# find_pos definition
X, Y, VIRUS = 0, 1, 2
N, K = map(int, input().split())

graph, virus_pos = [], []
for row in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    # 바이러스 걸리면 포지션 추가
    [virus_pos.append([row, col, 0]) for col, val in enumerate(data) if val > 0]

# 찾고자 하는 바이러스 정렬
virus_pos.sort(key=lambda x: graph[x[X]][x[Y]])
# S, X, Y
s, x, y = map(int, input().split())

cnt = bfs(graph, virus_pos, s)
print(graph[x - 1][y - 1])
