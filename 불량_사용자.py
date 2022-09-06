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
        # Get Hide Character Index
        hide_indexes = [i for i, char in enumerate(ban) if char == "*"]
        # "frodo"
        for user in user_id:
            # user가 ban의 길이랑 같지 않을경우 패스
            if not len(user) == len(ban):
                continue

            # "f"
            is_same = True
            for user_index, user_char in enumerate(user):
                # *이 아니면서 한글자라도 같지 않으면 틀린 문구라고 간주
                if user_char != ban[user_index] and not user_index in hide_indexes:
                    is_same = False
                    break

            if is_same:
                for r in results:
                    if user not in r:
                        each_possible.append(r + [user])
        results = each_possible

    for result in results:
        if set(result) not in answer:
            answer.append(set(result))

    return len(answer)
