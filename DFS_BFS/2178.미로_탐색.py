from collections import deque

# 동 남 서 북
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m = map(int, input().split())


def bfs(graph, visited):
    start = (1, 1)
    result = 0
    queue = deque([start])
    visited[1][1] = True

    temp = []
    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            # 동 남 서 북 순으로 break
            xx = x + dx
            yy = y + dy

            # x가 1보다 작고 n보다 클 경우
            # y가 1보다 작고 m보다 클 경우
            if xx < 1 or xx > n or yy < 1 or yy > m:
                continue

            if graph[xx][yy] == 1 and not visited[xx][yy]:
                # 되돌아갈지도 모르니 기존 임시 좌표 저장
                temp = [x, y]

                queue.append((xx, yy))
                visited[xx][yy] = True
                result += 1
                break

        # 없는 경우 돌아감
        if not queue:
            queue.append(temp)

    print(result)


graph = [[0] * (m + 1) for _ in range(n + 1)]
visited = [[False] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    nums = input()
    for index, each_num in enumerate(nums, start=1):
        graph[i][index] = int(each_num)

bfs(graph, visited)
