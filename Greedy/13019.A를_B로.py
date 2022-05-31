a = input()[::-1]
b = input()[::-1]

a = list(a)
b = list(b)
# 1. 받은 값들 역으로 정렬

# 2. 두개가 맞을 때 까지 임의 숫자 하나를 맨 끝으로 보냄
result = 0
temp = 0

if sorted(a) != sorted(b):
    print(-1)
    exit(0)

for i in range(len(a)):
    # 인덱스가 다를 경우
    if a[i] != b[temp]:
        result += 1
        continue

    temp += 1
    # 다를 경우 i번째 인덱스가 b랑 같은걸 찾음

print(result)
