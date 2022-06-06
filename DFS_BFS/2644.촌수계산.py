from collections import deque

n = int(input())
start, target = map(int, input().split())
m = int(input())

find = 0


def bfs(graph, v, visited):
    visited[v] = True

    queue = deque([v])
    result = [0 for _ in range(n + 1)]

    while queue:
        i = queue.popleft()
        # 같은 레벨의 인접노드 접근하기 전, count + 1
        # count += 1
        # 다른 노드로 들어가 방문처리 후 탐색
        for j in graph[i]:
            # if target == j:
            # return count

            if not visited[j]:
                queue.append(j)
                result[j] = result[i] + 1
                print(f"{j}     ::: ")
                print(result)
                visited[j] = True

    return result


graph = [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)

[graph[i].sort() for i in range(m)]

result = bfs(graph, start, visited)
print(result[target] if result[target] != 0 else -1)
