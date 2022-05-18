t = int(input())

result = []

for _ in range(t):
    n = int(input())

    data = [list(map(int, input().split())) for _ in range(n)]
    data.sort(key=lambda x: x[0])

    stack = []
    start_index = 0

    for j in range(0, len(data)):
        if data[j][1] > data[j + 1][1]:
            stack.append(data[j])
            start_index = j + 1
            break

    for i in range(start_index, len(data)):
        if stack[0][1] < data[i][1]:
            stack.clear()
            stack.append(data[i])
        else:
            stack.append(data[i])

    result.append(len(stack))

print("\n".join(str(r) for r in result))
