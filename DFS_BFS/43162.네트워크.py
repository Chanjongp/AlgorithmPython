from collections import deque


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()

        for index, i in enumerate(graph[v]):
            if index == v:
                continue
            # 방문하지 않았고 연결되어 있으면
            if not visited[index] and i == 1:
                queue.append(index)
                visited[index] = True


def solution(n, computers):
    answer = 0
    visited = [False] * n

    while True:
        try:
            index = visited.index(False)
            bfs(computers, visited, index)
            answer += 1

        except ValueError:
            break
    return answer
