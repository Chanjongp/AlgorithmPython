n = int(input())

data = []
rank_count = 1
result = 0

for _ in range(n):
    data.append(int(input()))

data = sorted(data)

for i in data:
    if i != rank_count:
        result += abs(i - rank_count)
    rank_count += 1

print(result)
