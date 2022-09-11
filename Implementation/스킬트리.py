# https://school.programmers.co.kr/learn/courses/30/lessons/49993
"""
skill_trees 1 ~ 20

C -> B -> D

# 1. 스킬트리 끝까지 찍은 케이스 -> CBADF
# 2. 스킬트리 끝까지는 안찍었지만 순서대로 찍은 케이스 -> AECB
"""


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        words = ""
        for char in skill_tree:
            if char in skill:
                words += char

        if skill[: len(words)] == words:
            answer += 1

    return answer
