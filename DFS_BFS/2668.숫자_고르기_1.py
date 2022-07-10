import copy

N = int(input())

graph = [[] for _ in range(N + 1)]
second = [int(input()) for _ in range(N)]
visited = [False] * (N + 1)
final_result = []
for index, i in enumerate(second, start=1):
    graph[i].append(index)

answer = set()


def dfs(graph, v, visited, result):
    visited[v] = True

    result.add(v)

    for i in graph[v]:
        print(i)
        # 방문 안했으면 DFS
        if not visited[i]:
            dfs(graph, i, visited, copy.deepcopy(result))
        # 방문 되어있으면 Cycle이 있는 것으로 확인하고 추가
        elif i in result:
            print(result)
            final_result.extend(list(result))
            return


for i in range(1, N + 1):
    if not visited[i]:
        dfs(graph, i, visited, answer)

print(final_result)
