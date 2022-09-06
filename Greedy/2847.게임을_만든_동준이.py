N = int(input())


data = [int(input()) for _ in range(N)]
answer = 0

for i in range(N - 1, 0, -1):
    # 전 단계보다 작거나 같다면
    if data[i] <= data[i - 1]:
        # (7 - 5) + 1
        temp = (data[i - 1] - data[i]) + 1
        answer += temp
        data[i - 1] -= temp


print(answer)
