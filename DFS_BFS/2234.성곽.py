import sys, copy

m, n = map(int, sys.stdin.readline().split())
X, Y = 0, 1

# 남 동 북 서
# 8  4  2  1
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


def dfs(graph, x, y, visited, room):
    visited[x][y] = True
    room.append((x, y))
    # 만약 어디든 갈 수 없으면 리턴
    for index, di in enumerate(directions):
        xx = x + di[X]
        yy = y + di[Y]
        # 벽 없으면
        if xx < 0 or xx >= n or yy < 0 or yy >= m:
            continue
        # 벽 없으면 && 방문 안했으면 DFS
        if graph[x][y][index] == "0" and not visited[xx][yy]:
            dfs(graph, xx, yy, visited, room)


# Initialize
graph = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    # 남 동 북 서
    data = list(map(int, sys.stdin.readline().split()))
    for index, i in enumerate(data):
        data[index] = bin(int(i))[2:].zfill(4)

    graph.append(data)


# BFS Execute
rooms = []
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            each_room = []
            dfs(graph, i, j, visited, each_room)
            rooms.append(each_room)

# 제일 큰 사이즈 정렬
rooms.sort(key=lambda x: len(x), reverse=True)

# 두개 합쳤을 때 제일 큰 경우의 수 저장
result = []
# 1. 방 개수
result.append(len(rooms))
# 2. 가장 넓은 방 길이
result.append(len(rooms[0]))

# 제일 큰 첫번째 사이즈 기준으로 합칠 수 있는 인덱스 찾음
adj_index = []

for i in range(result[0]):
    max_room = rooms[i]
    for room in rooms[(i + 1) :]:
        # 인접하는 인덱스 가져옴
        for x, y in max_room:
            for dx, dy in directions:
                xx = x + dx
                yy = y + dy
                if (xx, yy) in room and (xx, yy) not in adj_index:
                    adj_index.append((xx, yy))

        if adj_index:
            break


# 해당 인덱스 기준으로 BFS 수행
room_mix_cases = []
index_visited = [[False] * m for _ in range(n)]

for x, y in adj_index:
    # 2진수로 바꿈
    bin_val = graph[x][y]
    int_val = int("0b" + bin_val, 2)

    # 8 4 2 1
    for i in range(4):
        visited.clear()
        resize_room = []
        if bin_val[i] == "1":
            # 해당 자릿수 "0"으로 바꿈
            temp = int_val - pow(2, 4 - (i + 1))
            bin_temp = bin(int(temp))[2:].zfill(4)
            # 다시 2진수로 바꿔서 그래프에 넣음
            graph[x][y] = bin_temp
            dfs(graph, x, y, copy.deepcopy(index_visited), resize_room)

            # BFS 수행 후 기존 값 롤백
            graph[x][y] = bin_val
            room_mix_cases.append(len(resize_room))
result.append(max(room_mix_cases))
[print(r) for r in result]
