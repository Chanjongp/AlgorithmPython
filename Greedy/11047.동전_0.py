n, k = map(int, input().split(" "))


result = 0
coins = [int(input()) for _ in range(n)]

for coin in reversed(coins):
    result += k // coin
    k %= coin

print(result)
