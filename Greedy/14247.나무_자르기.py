"""
5
1 3 2 4 6
2 7 3 4 1
"""
import sys

N = int(input())

hi = list(map(int, sys.stdin.readline().split()))
ai = list(map(int, sys.stdin.readline().split()))

# 2차원 배열로 합침
data = []
[data.append([hi[i], ai[i]]) for i in range(N)]
data.sort(key=lambda x: x[1])

# 첫째날은 날짜 카운트가 안되고 시작
result = 0
for day, (hi, ai) in enumerate(data, start=0):
    result += hi + (ai * day)

print(result)
