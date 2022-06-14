n = int(input())
find_num = int(input())

data = [[0] * (n + 1) for _ in range(n + 1)]
find_arr = []

# 남 동 북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


data[n // 2][n // 2] = 1
x = 1
y = 1

turn_count = 1
dir = 0
length = n - 1

# 턴하는 기준 : turn_count가 length씩 4번 돌고 -> 몇번 도는지는 turn_count에 저장
# 한번 아래로 이동
# 이동하면 length로 감소 (2일 경우 끝)

for i in range((n ** 2), 1, -1):
    data[x][y] = i

    # 현재 수가 위치를 찾는거라면
    if i == find_num:
        find_arr = [x, y]

    x += dx[dir]
    y += dy[dir]

    # n - 1번 해당 방향으로 내려갔으면
    if turn_count == length:
        # 1로 초기화
        turn_count = 1

        # 방향이 이미 4번 돌았으면
        if dir == 3:
            # 한칸 아래로 및 초기화, length는 -2
            dir = 0
            x += 1
            y += 1
            length -= 2
            if length < 2:
                break
        else:
            # 안돌았으면 방향 바꿈
            dir += 1
    else:
        turn_count += 1

data[x][y] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(data[i][j], end=" ")
    print()

if not find_arr:
    find_arr.append(x)
    find_arr.append(y)

print(*find_arr)
