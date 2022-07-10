def solution(citations):
    citations.sort()

    more_h, less_h = [], []
    answer = 0
    cnt = 0

    is_zero = [True for v in citations if v > 0]
    if not is_zero:
        return 0

    for h in range(1, 10000):
        # 인용횟수 h보다 크고 작은지의 여부 체크
        [more_h.append(j) if j >= h else less_h.append(j) for j in citations]
        # 최댓값 비교
        # h:1   
        # 4 1
        if len(more_h) >= h and len(less_h) <= h:
            if h >= answer:
                cnt = 0
                answer = h
            elif cnt > 0:
                break
            else:
                cnt += 1

        # more 배열 초기화
        more_h.clear()
        less_h.clear()

    return answer
