# n : 행, m : 열
n, m = map(int, input().split())

# x : 행, y : 열
x, y, s = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

record = [[0] * m for _ in range(n)]
record[x][y] = 0

# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

result = 1
count = 0
while True:
    # 1. 현재 위치에서 왼쪽 방향
    s -= 1
    if s == -1:
        s = 3

    # 왼쪽 한칸
    nx, ny = (x + dx[s]), (y + dy[s])
    print(nx, ny)
    if (nx < 0 or nx > n) or (ny < 0 or ny > m):
        count += 1
    # 2 - 1. 왼쪽 안가봄
    elif record[nx][ny] == 0 and data[nx][ny] == 0:
        # 왼쪽 이동 및 기록
        x, y = nx, ny
        record[nx][ny] = 1
        # count 초기화
        result += 1
        count = 0
    # 2 - 2. 왼쪽 가봤거나 바다
    else:
        # 왼쪽 방향만 이동 및 카운트
        count += 1

    # 3. 카운트 4개일 때
    if count == 4:
        # 뒤로 한칸 -> 1단계
        back_s = s + 2
        if s > 3:
            back_s -= 4

        nx, ny = (x + dx[back_s]), (y + dy[back_s])

        # 뒤도 바다 -> 끝
        if record[nx][ny] == 1 or data[nx][ny] == 1:
            break

        continue

print(result)
