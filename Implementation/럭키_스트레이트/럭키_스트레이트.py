n = str(input())

# str
half = len(n) // 2

first = n[:half]
second = n[half:]

first_value = 0
second_value = 0

for num in first:
    first_value += int(num)

for num in second:
    second_value += int(num)

if first_value == second_value:
    result = "LUCKY"
else:
    result = "READY"


print(result)
