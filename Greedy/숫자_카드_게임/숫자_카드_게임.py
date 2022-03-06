# N: 행, M : 열
n, m = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
arr = []
each_small_column = []

# n행 만큼 한줄씩 입력받기
for i in range(0, n):
    # 한 행을 배열로 받음
    row = list(map(int, input().split()))
    # 배열에 추가
    arr.append(row)
    # 현재 행에서 가장 작은 수를 기록하는 배열에 넣어줌
    each_small_column.append(min(arr[i]))

# 각 행마다 작은 값들 중에, 큰 수 찾아서 print
print(max(each_small_column))
