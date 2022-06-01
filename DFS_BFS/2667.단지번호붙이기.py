from collections import deque

n = int(input())

# 동 남 서 북
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
results = []
results_size = 0


def bfs(graph, visited, start):
    queue = deque([start])

    result = 1
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            xx = x + dx
            yy = y + dy

            # 예외처리
            if xx < 0 or xx > (n - 1) or yy < 0 or yy > (n - 1):
                continue

            # print(xx, yy)
            if graph[xx][yy] == 1 and not visited[xx][yy]:
                queue.append([xx, yy])
                visited[xx][yy] = True
                result += 1

    return result


graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

# 데이터 인풋
for i in range(n):
    data = input()
    for index, str_num in enumerate(data):
        graph[i][index] = int(str_num)


# 시작
# print(graph)
for i in range(n):
    for j in range(n):
        # 방문 안한 좌표고 1이면
        if graph[i][j] == 1 and not visited[i][j]:
            result = bfs(graph, visited, (i, j))
            results.append(result)

results.sort()
print(len(results))
[print(r) for r in results]
