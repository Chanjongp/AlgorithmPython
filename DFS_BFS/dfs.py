# graph
# v: 현재 방문 위치
# visited: 방문된 위치

count = 0


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True

    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


graph = [
    # 문제 그래프가 1번부터 시작하니 헷갈리지 않도록 0번 패스
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

visited = [False] * len(graph)

dfs(graph, 1, visited)
