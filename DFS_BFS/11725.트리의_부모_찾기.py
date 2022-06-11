import sys

sys.setrecursionlimit(100001)


def dfs(graph, v, visited):
    for i in graph[v]:
        # dfs로 들어가기 전에, 결과에 아무 값이 안들어가 있으면 부모 노드 저장
        if visited[i] == 0:
            visited[i] = v
            dfs(graph, i, visited)


# Initialize
N = int(sys.stdin.readline())
graph = [[] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)


# Input Data
for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

# Execute
dfs(graph, 1, visited)
for i in range(2, len(visited)):
    print(visited[i])
