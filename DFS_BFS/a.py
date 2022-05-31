result = 0


def dfs(graph, start, value, target):
    # 절댓값이면 리턴
    if abs(start) == len(graph):
        if value == target:
            global result
            result += 1
        return

    value_1 = value + graph[start]
    value_2 = value - graph[start]

    # # 정수한번 음수한번
    dfs(graph, start + 1, value_1, target)
    dfs(graph, start + 1, value_2, target)


def solution(numbers, target):
    dfs(numbers, 0, 0, target)


numbers = [1, 1, 1, 1, 1]
target = 3
solution(numbers, target)
print(result)
