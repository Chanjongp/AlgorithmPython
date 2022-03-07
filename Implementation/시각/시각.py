n = int(input())

# 경우의 수
# 24 x 60 x 60
result = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                result += 1

print(result)
