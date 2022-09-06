import sys
import heapq

N, D = map(int, sys.stdin.readline().split())
INF = 1e9

# Initialize
graph = [[] for _ in range(D + 1)]
distance = [INF] * (D + 1)

[graph[i].append((i + 1, 1)) for i in range(D)]

for i in range(N):
    # 시작, 끝, 지름길의 길이
    start, end, short = map(int, sys.stdin.readline().split())
    if end > D:
        continue
    # 그래프의 시작점에 끝, 지름길 추가
    graph[start].append((end, short))


def dijkstra(start, queue):
    distance[start] = 0

    # (거리, 노드)로 넣음
    # 거리부터 하게 되면 오름차순 정렬
    heapq.heappush(queue, (0, 0))
    while queue:
        short, node = heapq.heappop(queue)
        if distance[node] < short:
            continue

        # 노드를 더함
        for i in graph[node]:
            # 지름길 통해서 가는게 빠르니, 지름길을 거리랑 더함
            cost = short + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dijkstra(0, [])
print(distance[D])
