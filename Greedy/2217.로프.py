n = int(input())

weights = [int(input()) for _ in range(n)]
weights.sort()

num = len(weights)
result = 0
for i in range(len(weights)):
    v = weights[i] * (num - i)
    if v > result:
        result = v

print(result)
