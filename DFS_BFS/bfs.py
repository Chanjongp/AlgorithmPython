from collections import deque

queue = deque()


def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # start 방문처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue:
        # queue에서 노드를 꺼냄
        v = queue.popleft()
        print(v, end=" ")
        # 인접 노드 리스팅
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

bfs(graph, 1, visited)
