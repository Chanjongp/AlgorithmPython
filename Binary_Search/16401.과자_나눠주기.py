import sys

# 조카 명수, 과자 개수
N, M = map(int, input().split())
data = list(map(int, sys.stdin.readline().split()))
result = 0


start, end = 0, max(data)
while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        break

    count = 0
    for i in data:
        count += (i // mid) if i >= mid else 0

    # 막대 개수가 일치할 경우
    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
