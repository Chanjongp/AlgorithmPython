# https://school.programmers.co.kr/learn/courses/30/lessons/64064
"""
제재 아이디
frodo, fradi -> fr*d*
abc123 -> abc1**

user_id: 1 ~ 8
len: 1 ~ 8

banned_id: 1 ~ 8
하나이상 '*' 포함
"""


def solution(user_id, banned_id):
    answer = []
    results = [[]]
    for ban in banned_id:
        each_possible = []
        # 숨겨진 문자의 인덱스 찾기
        hide_indexes = [i for i, char in enumerate(ban) if char == "*"]

        for user in user_id:
            # user가 ban의 길이랑 같지 않을경우 패스
            if not len(user) == len(ban):
                continue

            is_same = True
            for user_index, user_char in enumerate(user):
                # *이 아니면서 한글자라도 같지 않으면 틀린 문구라고 간주
                if user_char != ban[user_index] and not user_index in hide_indexes:
                    is_same = False
                    break

            # 해당 문자에 포함될 수 있으면
            if is_same:
                # []
                for r in results:
                    # frodo, fradi를 새로운 배열로 추가
                    if user not in r:
                        # 두번쨰 *rodo에 해당하는 user_id를 각각의 기존 배열에 추가 (없을 경우만)
                        # ex. [["fradi"], ["frodo"]] => [["fradi", "frodo"], ["frodo", "crodo"]]
                        # ["frodo"] + ["fredi"] => append 하면서 [["frodo", "fredi"]]
                        each_possible.append(r + [user])

        # ban의 한 단어가 끝나면 포함되는 결과값을 results에 저장
        results = each_possible

    for result in results:
        # 각 배열을 answer 배열에 set으로 추가
        # 문제에서 "나열된 순서와 관계없이" 라고 했으므로, set으로 캐스팅
        if set(result) not in answer:
            answer.append(set(result))

    return len(answer)


print(
    solution(
        ["frodo", "fradi", "crodo", "abc123", "frodoc"],
        ["fr*d*", "*rodo", "******", "******"],
    )
)
