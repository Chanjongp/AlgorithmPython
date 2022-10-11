# https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""
ROR 게임 -> 상대 팀 진영을 먼저 파괴

5 x 5
나: (1, 1), 상대: (5, 5)

검은색: 벽
흰색: 통로

동서남북
"""
from collections import deque

# 동 남 서 북
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(maps, start, N, M):
    queue = deque([start])
    while queue:
        x, y = queue.popleft()

        for dx, dy in dirs:
            xx = x + dx
            yy = y + dy

            # 예외처리
            if xx < 0 or xx >= N or yy < 0 or yy >= M:
                continue
            # 맵이 이미 방문했거나 돌이면
            elif maps[xx][yy] == 0 or maps[xx][yy] > 1:
                continue

            maps[xx][yy] = maps[x][y] + 1
            if xx == N - 1 and yy == M - 1:
                return maps[xx][yy]

            queue.append((xx, yy))

    return -1


def solution(maps):
    answer = 0

    N, M = len(maps), len(maps[0])

    # BFS, 2부터 시작 => 1이 벽이기 때문에
    maps[0][0] = 1
    answer = bfs(maps, (0, 0), N, M)

    return answer
