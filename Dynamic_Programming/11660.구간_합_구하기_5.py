# import sys

# n, m = map(int, sys.stdin.readline().split())


# data = []
# find = []
# results = []

# # 동 남 서 북
# directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
# for i in range(n):
#     line = list(map(int, sys.stdin.readline().split()))
#     # 첫째 줄일 때
#     if i == 0:
#         for i in range(1, len(line) + 1):
#             line[i] = line[i] + line[i - 1]

#         data.append(line)
#     # 둘째 줄부터
#     else:
#         for j in range(n):


# # for _ in range(m):
# #     line = list(map(int, sys.stdin.readline().split()))

# #     start = line[:2]
# #     target = line[2:]

# #     count = 0

# #     while start != target:
# #         x, y = start[0], start[1]
# #         count += data[x][y]
