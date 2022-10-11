# https://school.programmers.co.kr/learn/courses/30/lessons/81301

NUMBER = 0
LENGTH = 1


def solution(s):
    answer = ""
    size, height = len(s), 0
    if s.isdigit():
        return int(s)

    # val, length
    alpha_dict = {
        "zero": ("0", 4),
        "one": ("1", 3),
        "two": ("2", 3),
        "three": ("3", 5),
        "four": ("4", 4),
        "five": ("5", 4),
        "six": ("6", 3),
        "seven": ("7", 5),
        "eight": ("8", 5),
        "nine": ("9", 4),
    }
    alph_keys = alpha_dict.keys()

    i = 0
    a = []
    while i < size:
        # 숫자로 변환 가능하면 패스
        if s[i].isdigit():
            answer += str(s[i])
            i += 1

        # 맞는단어 체크 (최소자리수 3)
        else:
            j = i + 3

            while True:
                # i => 0
                # j => 3

                # s[0:3] => "ONE"
                word = s[i:j]
                if word in alph_keys:
                    # 알파벳으로 변환 및 점프
                    answer += alpha_dict[word][NUMBER]
                    i += alpha_dict[word][LENGTH]
                    break
                else:
                    # 아닐 경우에는 다음단어까지 체크
                    j += 1

    return int(answer)


a = [1, 2, 3]

a.ch
