import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    result = 0

    while scoville[0] < K:
        # 배열 사이즈랑 크거나 같으면
        if len(scoville) <= 1:
            return -1
        # 가장 작은 값 2개 pop
        first_val = heapq.heappop(scoville)
        second_val = heapq.heappop(scoville)

        # 새로운 음식 스코빌
        sum_val = first_val + (second_val * 2)
        # heap push
        heapq.heappush(scoville, sum_val)
        result += 1
    # 가진 음식의 스코빌 지수
    return result


scoville = [1, 2, 3, 9, 10, 12, 13, 14]
result = solution(scoville, 7)
print(result)
