import sys

# 스태프 수, 풍선 개수
n, m = map(int, sys.stdin.readline().split())
staffs = list(map(int, sys.stdin.readline().split()))

start = 0
end = int(1e6 ** 2)
result = 0
while start <= end:
    # 중간 시간
    mid_time = (start + end) // 2

    # 풍선들
    ballons = sum([mid_time // staff for staff in staffs])

    # 타겟의 풍선 수가 더 크거나 같으면
    if ballons >= m:
        end = mid_time - 1
        result = mid_time
    # 타겟의 풍선 수가 더 작으면
    else:
        start = mid_time + 1

print(result)
