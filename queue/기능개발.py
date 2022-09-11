"""
뒤에 있는 기능이 먼저 개발될 수 있음
이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

:: progresses
:: speeds

100, 100
"""
from math import ceil

COMPLETE = 100


def solution(progresses, speeds):
    answer, complete_day = [], []

    complete_day = [
        ceil((COMPLETE - task) / speed) for task, speed in zip(progresses, speeds)
    ]

    latest, cnt = complete_day[0], 1
    for now in complete_day[1:]:
        # 전에있는 태스크가 크다면 해당 일자에 테스크 완수
        if latest >= now:
            cnt += 1
        else:
            answer.append(cnt)
            latest = now
            cnt = 1

    answer.append(cnt)
    return answer
