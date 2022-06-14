n = int(input())

result = 0
for _ in range(n):
    val = input()

    is_group = True
    # 나온 알파벳 저장
    temp = set()
    # num: 연속되는 카운팅 하는 변수
    # last_str: 전 단어를 체크하는 변수
    num, last_str = 0, ""
    for v in val:
        # 단어가 temp에 있는데 연속되는 숫자라면
        if v in temp and last_str == v:
            num += 1
        # 단어가 temp에 있는데 연속되지 않은 숫자라면
        if v in temp and num < 2:
            is_group = False
            break
        # 처음 나오는 숫자라면
        else:
            temp.add(v)
            last_str = v
            num = 1
    result += 1 if is_group else 0

print(result)
