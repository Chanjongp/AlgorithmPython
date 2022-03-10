from collections import deque

n, m = map(int, input().split())

graph = [[]]

for i in range(n):
    col = [int(v) for v in map(str, input())]
    col.insert(0, 99)
    graph.append(col)


def bfs(graph, start):
    queue = deque([start])

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        [x, y] = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue

            if graph[nx][ny] == 0:
                continue

            # 탈출하기 위해 한칸 갔을 때 괴물이 없으면
            if graph[nx][ny] == 1:
                # 큐에 추가
                queue.append([nx, ny])
                # 큐에서 가져온 값 방문처리
                graph[nx][ny] = graph[x][y] + 1

    return graph[n - 1][m - 1]


print(bfs(graph, start=[1, 1]))
