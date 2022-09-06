import heapq
import sys


INF = 1e9

N = int(input())
graph = [[] * (N) for _ in range(N)]
distance = [INF] * (N)

for i in range(N):
    data = list(sys.stdin.readline())

    # 2, 3
    friends = [index for index, i in enumerate(data) if i == "Y"]
    if len(friends) == 1:
        continue

    for friend in friends:
        graph[friend].append()


print(graph)
