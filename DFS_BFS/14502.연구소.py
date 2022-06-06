import copy
from collections import deque

# x, y
n, m = map(int, input().split())

# 동 남 서 북
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

graph = []
empty = []
virus = []
final_result = 0
# 데이터 초기화
for i in range(n):
    data = list(map(int, input().split()))
    graph.append(data)

    for index, j in enumerate(data):
        if j == 2:
            virus.append((i, index))
        elif j == 0:
            empty.append((i, index))

# bfs
def bfs(temp_graph):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            xx = x + dx
            yy = y + dy
            # 예외처리
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue

            if temp_graph[xx][yy] == 0:
                temp_graph[xx][yy] = 2
                queue.append((xx, yy))

    result = 0
    for i in range(n):
        result += temp_graph[i].count(0)

    global final_result
    final_result = max(final_result, result)


# 데이터 0중에 무작위로 3번 1로 바꿈
for i in range(len(empty)):
    for j in range(i):
        for k in range(j):
            temp_graph = copy.deepcopy(graph)
            # 3개 좌표 임시
            temp = [empty[i], empty[j], empty[k]]
            # 3개 좌표 1로 변경
            for x, y in temp:
                temp_graph[x][y] = 1

            # bfs 수행
            bfs(temp_graph)

print(final_result)
