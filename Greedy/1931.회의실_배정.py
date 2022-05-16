n = int(input())

data = [list((map(int, input().split()))) for _ in range(n)]

# 시작하는 회의시간 끝나는 시간을 기준으로 오름차순 정렬
# 이 때, 끝나는 시간이 같으면 시작시간을 내림차순으로 재정렬
data.sort(key=lambda x: (x[1], -x[0]))

result = 1
last_number = data[0][1]

# 같은시간에 시작면 작은것부터
for i in range(1, n):
    if data[i][0] >= last_number:
        last_number = data[i][1]
        result += 1

print(result)
