"""
0 ~ N - 1

n: 사람 수
m: 친구 관계 수

A는 B와 친구다.
B는 C와 친구다.
C는 D와 친구다.
D는 E와 친구다.

5 4
0 1
1 2
2 3
3 4
"""
n, m = map(int, input().split())
graph = [[] * (n + 1) for _ in range(n)]
visited = [False] * n

result = 0


def dfs(graph, v, visited, cnt):
    # 예외처리
    visited[v] = True
    # 관계 체크
    if cnt >= 4:
        # 메모리 초과 부분
        print(1)
        exit(0)

    for data in graph[v]:
        if not visited[data]:
            dfs(graph, data, visited, cnt + 1)

    visited[v] = False


for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(n):
    dfs(graph, i, visited, 0)
