from collections import deque

# y x
m, n = map(int, input().split())

# 동 남 서 북
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs(graph, initial_visited):
    # 큐가 들어있는 배열 정의
    queue = deque(initial_visited)
    result = 0
    while queue:
        x, y = queue.popleft()
        # 동남서북 기준
        for dx, dy in directions:
            # 막혀있으면
            xx = x + dx
            yy = y + dy
            # 예외처리
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue

            # 벽 or 예외처리
            elif graph[xx][yy] in [-1, 1]:
                continue

            # 익힐 수 있는 토마토면
            if graph[xx][yy] == 0:
                queue.append((xx, yy))
                # 몇번 탐색했는지 저장하면서 탐색
                graph[xx][yy] = graph[x][y] + 1
                # 최댓값 계속 저장하면서 탐색
                if graph[xx][yy] > result:
                    result = graph[xx][yy]

    for i in range(n):
        if 0 in graph[i]:
            return -1

    return result - 1


graph = []
initial_visited = []

is_not_in_0 = 0

for i in range(n):
    data = list(map(int, input().split()))

    # 1인 좌표 넣어야 함
    for index, j in enumerate(data):
        if j == 1:
            initial_visited.append((i, index))

    graph.append(data)
    # 한 줄에 0이 없으면 +1 카운트
    if not 0 in data:
        is_not_in_0 += 1

# 0이 없어서 카운트된 값이 세로값(n)일 경우 0 출력
if is_not_in_0 == n:
    print(0)
else:
    result = bfs(graph, initial_visited)
    print(result)
