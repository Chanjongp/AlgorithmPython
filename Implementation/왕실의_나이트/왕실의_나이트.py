n = str(input())

column_to_int = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

x, y = column_to_int[n[0]], int(n[1])

cases = {
    # X
    "L": [(-2, 1), (-2, -1)],
    "R": [(2, 1), (2, -1)],
    # Y
    "U": [(1, -2), (-1, -2)],
    "D": [(1, 2), (-1, 2)],
}

result = 0
for case in cases.keys():
    # L, R, U, D 4가지 실행
    action = cases[case]

    # 각 케이스마다 2번씩 실행
    for i in range(2):
        dx, dy = x + action[i][0], y + action[i][1]
        if (dx < 1 or dx > 8) or (dy < 1 or dy > 8):
            continue

        result += 1

print(result)
