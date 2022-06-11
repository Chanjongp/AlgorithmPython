"""
10 7
1 3 5 7 9 11 13 15 17 19
4
"""


def binary_search(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 찾아야 할 값이 중간점이면
    if data[mid] == target:
        return mid
    # 데이터가 중간점보다 오른쪽에 있으면
    elif data[mid] < target:
        # 끝점을 중간점 -1로 변경
        return binary_search(data, target, mid + 1, end)

    # 데이터가 중간점보다 왼쪽에 있으면
    else:
        return binary_search(data, target, start, mid - 1)


n, m = map(int, input().split())
data = list(map(int, input().split()))

result = binary_search(data, m, 0, n - 1)
if result is None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
