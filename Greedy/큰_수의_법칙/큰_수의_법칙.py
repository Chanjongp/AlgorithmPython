n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

# 5 8 3 (8번 까지 더하고, 3번 연속 숫자 더하기 가능)
# 2 4 5 4 6
# 6 6 6 5 6 6 6 5

k_count, m_count, result = 0, 0, 0
n_count = 0

# 가장 큰 숫자로 order
sorted_arr = sorted(arr, reverse=True)

for i in range(m):
    result += sorted_arr[n_count]
    k_count += 1

    if k_count == k:
        n_count += 1
        k_count = 0
    elif n_count == 1:
        n_count = 0
        k_count = 0

print(result)
