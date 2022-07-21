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


""" 한달 후에 푼거"""

from collections import deque


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return None


def solution(n, computers):
    answer = 0
    graph = [[] * n for _ in range(n)]
    visited = [False] * n

    # computers -> graph 치환
    for i, computer in enumerate(computers):
        [
            graph[i].append(j)
            for j, is_connect in enumerate(computer)
            if is_connect and j != i
        ]

    for k in range(n):
        if not visited[k]:
            bfs(graph, visited, k)
            answer += 1

    return answer
