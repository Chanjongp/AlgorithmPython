import sys

n, l = map(int, sys.stdin.readline().split())

result = 1
data = list(map(int, sys.stdin.readline().split()))
data.sort()

start, end = data[0], data[0] + l

# 모든 테이프 돌 떄 까지
for i in range(1, n):
    if start <= data[i] < end:
        continue

    start, end = data[i], data[i] + l
    result += 1

print(result)
