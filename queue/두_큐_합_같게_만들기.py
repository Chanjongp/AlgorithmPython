"""
q1: 원소 추출
q2: 집어넣음

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

=> 4, 6, 5 

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

현재 큐의 총합과 중간값을 빼서 -인 q에서 +인 q로 이동
"""
from collections import deque


def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)

    answer = 0

    middle = (sum1 + sum2) / 2

    for _ in range(3 * len(queue1)):
        # 중간값 구함 (10)
        if sum1 == sum2:
            return answer
        elif sum1 == 0 or sum2 == 0:
            return -1

        # +4, -4
        diff_queue1 = middle - sum1
        diff_queue2 = middle - sum2

        # diff_queue2가 더 작으면
        # queue2 -> queue1로 이동 (pop and append)
        if diff_queue1 > diff_queue2:
            val = queue2.popleft()
            sum1 += val
            sum2 -= val
            queue1.append(val)
        else:
            val = queue1.popleft()
            sum2 += val
            sum1 -= val
            queue2.append(val)

        answer += 1

    return -1


"""
2022.12.24 재풀이

"""
from collections import deque
    
MAX_LENGTH = 300000

def move(pop_q, insert_q):
    val = pop_q.popleft()
    insert_q.append(val)
    return val
    

def solution(queue1, queue2):
    result = 0
    q1, q2 = deque(queue1), deque(queue2)

    sum_q1, sum_q2 = sum(q1), sum(q2)
    # 시작부터 같을 경우, 0 리턴
    if sum_q1 == sum_q2:
        return 0

    while result != MAX_LENGTH:
        # 1. 큰 큐 선택
        # 2. 이동
        if sum_q1 > sum_q2:
            pop_val = move(q1, q2)
            sum_q1 -= pop_val
            sum_q2 += pop_val
        else:
            pop_val = move(q2, q1)
            sum_q2 -= pop_val
            sum_q1 += pop_val
        
        result += 1
        # 3. 큐 값이 같아졌는지 체크
        if (sum_q1 == sum_q2):
            break
        
    if result == MAX_LENGTH:
        return -1

    return result
    