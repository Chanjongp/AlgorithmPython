n = map(int, input())

data = list(map(int, input().split()))

data.sort(reverse=True)


result = 0
# 가장 큰 숫자부터 시작해서, 작은숫자부터 그루핑
for i in range(0, len(data)):
    value = data.pop(0)

    for j in range(0, value):
        data.pop(-1)

    result += 1


print(result)
