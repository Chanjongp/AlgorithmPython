n = int(input())
actions = map(str, input().split())

result = [1, 1]

action_type = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

for action in actions:
    is_ignored = False
    # X축 예외처리
    if (result[1] == 1 and action == "L") or (result[1] == n and action == "R"):
        is_ignored = True
    # Y축 예외처리
    elif (result[0] == 1 and action == "U") or (result[0] == n and action == "D"):
        is_ignored = True

    # N x N을 벗어낫을 경우 무시
    if is_ignored:
        continue

    action_point = action_type[action]
    result[0] += action_point[0]
    result[1] += action_point[1]

    print(result)
