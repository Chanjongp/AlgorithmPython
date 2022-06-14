import sys

n = int(sys.stdin.readline())


dir, people = [0], [0]
# n
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    dir.append(data[0])
    people.append(data[1])

result = 1
min_dir = 0

# 케이스 1 ~ n + 1일 경우 체크
# n ** 2
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        cnt += abs(i - j) * people[j] if not i == j else 0

    if min_dir > 0 and cnt < min_dir:
        min_dir = cnt
        result = i
    else:
        min_dir = cnt

print(result)
print(min_dir)
