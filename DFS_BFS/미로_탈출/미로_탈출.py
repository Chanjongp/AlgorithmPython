from collections import deque

n, m = map(int, input().split())

graph = [[]]

for i in range(n):
    col = [int(v) for v in map(str, input())]
    col.insert(0, 99)
    graph.append(col)


x = 0
y = 1

print(graph)


def bfs(graph, start, end):
    result = 1
    queue = deque([start])

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        point = queue.popleft()
        # 큐에서 가져온 값 방문처리
        graph[point[x]][point[y]] = 0

        # 마지막 까지 가면 결과 리턴
        if point == end:
            return result

        for i in range(len(dx)):
            nx = point[x] + dx[i]
            ny = point[y] + dy[i]

            if (nx < 1 or nx > n) or (ny < 1 or ny > m):
                continue

            # 탈출하기 위해 한칸 갔을 때 괴물이 없으면
            if graph[nx][ny] == 1:
                # 큐에 추가
                queue.append([nx, ny])

                result += 1

        return result


print(bfs(graph, start=[1, 1], end=[n, m]))
