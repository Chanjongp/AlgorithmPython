n = int(input())
find_num = int(input())
# Initialize
data = [[0] * (n + 1) for _ in range(n + 1)]
find_pos = []

# 남 동 북 서
directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
x = 1
y = 1
# dx dy 상수, 방향 카운트, 방향 설정
dx, dy = 0, 1
dir_count = 1

direction = 0
rec_size = n - 1

for val in range(n ** 2, 1, -1):
    data[x][y] = val

    # 찾는 수가 맞는지 확인
    if find_num == val:
        find_pos.append(x)
        find_pos.append(y)

    x += directions[direction][dx]
    y += directions[direction][dy]

    # dir_count가 n - 1 만큼 돌았으면 방향 체인지
    if dir_count == rec_size:
        dir_count = 1

        # 방향이 상하좌우 4번 다 돌았으면
        if direction == 3:
            # 방향 초기화 및 좌표 변경
            direction = 0
            x, y = x + 1, y + 1
            rec_size -= 2
            if rec_size < 2:
                break
        else:
            direction += 1
    # 아니면 dir_count 추가
    else:
        dir_count += 1


data[x][y] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(data[i][j], end=" ")
    print()

if not find_pos:
    find_pos = [x, y]

print(*find_pos)
