n, k = map(int, input().split())

circle = [i for i in range(1, n + 1)]
size = len(circle)
cursor = k - 1
stack = []

while circle:
    # k번째 데이터 pop (배열 크기 1 줄임)
    data = circle.pop(cursor)
    stack.append(data)
    size -= 1
    cursor += k - 1

    while size <= cursor:
        cursor -= size
        if size == 0:
            break


result = str(stack).replace("[", "<").replace("]", ">")
print(result)
