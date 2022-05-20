t = int(input())

results = []

for _ in range(t):
    n = int(input())

    data = [list(map(int, input().split())) for _ in range(n)]
    data.sort()

    result = 1
    last_index = data[0][1]
    for i in range(1, n):
        # 스택 끝에있는 값이 현재 인덱스보다 등수가 작으면
        if last_index > data[i][1]:
            last_index = data[i][1]
            result += 1

    results.append(result)

print("\n".join(str(r) for r in results))
