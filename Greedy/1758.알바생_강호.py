n = int(input())

data = [int(input()) for _ in range(n)]
data.sort(reverse=True)

for index, i in enumerate(data):
    n = i - index
    if n > 0:
        data[index] = n
    else:
        data[index] = 0

print(sum(data))
