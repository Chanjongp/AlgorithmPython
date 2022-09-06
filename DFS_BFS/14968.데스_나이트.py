from collections import deque

N = int(input())

data = list(map(int, input().split()))

directions = ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1))
visited = [[0] * N for _ in range(N)]


def bfs(start, end, visited):
    queue = deque([start])
    visited[start[0]][start[1]] += 1

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            rr = r + dr
            cc = c + dc

            if rr < 0 or rr >= N or cc < 0 or cc >= N:
                continue
            elif visited[rr][cc] > 0:
                continue

            visited[rr][cc] = visited[r][c] + 1
            if [rr, cc] == end:
                print(visited[rr][cc] - 1)
                exit(0)
            queue.append((rr, cc))

    return None


start = data[:2]
end = data[2:]

bfs(start, end, visited)
print(-1)
