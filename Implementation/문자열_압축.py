# Level 2
# https://programmers.co.kr/learn/courses/30/lessons/60057#


def solution(s):
    size = len(s)
    if size <= 2:
        return size

    result = 0
    # i : 단위
    # j : 실제 카운트
    for i in range(1, len(s)):
        temp = i
        progress = 0  # 연속 몇번 되었는지
        # i : 2, s : 11 (0 ~ 10)
        # cnt: 5
        # rest: s[(i x cnt-1):]
        # i의 단위로 몇 번 돌 수 있는지 확인
        # 초기값 저장
        last = s[0:i]
        # i(1)부터 시작하여 cnt까지 i(1)단위의 간격을 주면서 돔
        for j in range(i, size - size % i, i):
            # i개 단위로 자른 문자열 나옴
            sepr = s[j : (j + i)]

            # i개 단위로 끊었을 떄, 전 문장이랑 같는지 체크
            # 다르면 해당 문자열 temp에 더하고 초기화
            if not sepr == last:
                last = sepr
                progress = 0
                temp += i
                continue

            # 전 문장이랑 같은데 첫 연속이면 +1만 함
            if progress < 1:
                temp += 1
            # 10번 이상의 연속일 경우  -> 0부터 시작했으므로 8
            elif progress == 8:
                temp += 1

            progress += 1
            last = sepr

        temp += len(s[size - size % i :])

        if result > 1:
            result = min(temp, result)
        else:
            result = temp

    return result
