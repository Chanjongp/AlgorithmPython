import copy
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    result = 0
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            # 방문하지 않음과 동시에 신뢰를 "당하고" 있을 때
            if not visited[i] and i in trust[v]:
                result += 1
                queue.append(i)
                visited[i] = True
    return result


n, m = map(int, input().split())

graph = [[] * n for _ in range(n + 1)]
trust = copy.deepcopy(graph)

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

    trust[n2].append(n1)

visited = [False] * (n + 1)
a_result = [bfs(graph, i, copy.deepcopy(visited)) for i in range(1, n + 1)]


max_value = 0
index_arr = []
for index, value in enumerate(a_result):
    if value >= max_value:
        if value > max_value:
            index_arr.clear()
            max_value = value

        index_arr.append(index + 1)

[print(index, end=" ") for index in index_arr]
