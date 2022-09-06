# https://school.programmers.co.kr/learn/courses/30/lessons/43238


def binary_search(times, n, start, end):
    """
    start : 1
    end : 60

    mid
    1: 1 ~ 30 cnt 7
    2: 1 ~ 29 cnt 6
    3: 1 ~ 28 cnt 6
    """
    answer = 0
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for time in times:
            # 4 + 3
            cnt += mid // time

        # n명보다 크거나 같으면 더 시간을 줄일 수 있으므로 왼쪽으로
        if cnt >= n:
            answer = mid
            end = mid - 1
        # n명보다 작을 때는 더
        else:
            start = mid + 1

    return answer


def solution(n, times):
    # 최소 시간 ~ 최악의 시간
    # 1, n * max(times) = 60
    start, end = 1, n * max(times)
    answer = binary_search(times, n, start, end)
    return answer


print(solution(6, [7, 10]))
