"""
1
5 3
8 1 7 3 1
3 6 1
"""


def binary_search(data, target):
    start = 0
    end = len(data) - 1

    result = -1

    while start <= end:
        # 클 경우
        mid = (start + end) // 2
        if data[mid] < target:
            result = mid
            start = mid + 1
        # 작을 경우
        else:
            end = mid - 1

    return result


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    answer = 0
    for i in A:
        # Index + 1
        # Index가 0일 경우와 비교하기 위해 result를 -1로 선언하고, 바깥에서 1 더함
        a = binary_search(B, i) + 1
        answer += a

    print(answer)
