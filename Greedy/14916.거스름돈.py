# 5 이하일 경우 케이스를 생각하지 못했음 -> 7트

# 13
n = int(input())

# 0, 3
count_1, n = divmod(n, 5)

if (n % 2) != 0:
    # 5보다 클 경우
    if not count_1 == 0:
        # 3 + 5 = 8 (n)
        n += 5
        count_1 -= 1

count_2, n = divmod(n, 2)

if n != 0:
    print(-1)
else:
    print(count_1 + count_2)
