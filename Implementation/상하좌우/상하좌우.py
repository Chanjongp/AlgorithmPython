n = int(input())
moves = list(map(str, input().split()))

data = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        data.append([i, j])

# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


x, y = 1, 1

for move in moves:
    if move == "L" and y != 1:
        x += dx[2]
        y += dy[2]
    elif move == "R" and y != n:
        x += dx[0]
        y += dy[0]
    elif move == "U" and x != 1:
        x += dx[1]
        y += dy[1]
    elif move == "D" and x != n:
        x += dx[3]
        y += dy[3]

print(x, y)
