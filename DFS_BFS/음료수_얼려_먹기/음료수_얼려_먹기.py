n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = []
for i in range(n):
    visited.append([False if not graph[i][j] else True for j in range(m)])


result = 0


def bfs(graph, v, visited):
    # 상 하 좌 우
    visited[v[0]][v[1]] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        # 상하좌우 한칸씩
        nx = v[0] + dx[i]
        ny = v[1] + dy[i]

        if (nx < 0 or nx >= n) or (ny < 0 or ny >= m):
            continue

        if graph[nx][ny] == 0 and not visited[nx][ny]:
            bfs(graph, [nx, ny], visited)
            global result
            print(f"({nx}, {ny})")
            result += 1


start_x = 1
start_y = 1

bfs(graph, [start_x, start_y], visited)


print(result)
