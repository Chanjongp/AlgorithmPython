n = int(input())

data = list(map(int, input().split()))
data.sort()


times = []

result = 0
for i in data:
    result += i
    times.append(result)

print(sum(times))
