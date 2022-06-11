def solution(clothoes):
    categories = {}
    for i in range(len(clothoes)):
        if categories.get(clothoes[i][1], None):
            categories[clothoes[i][1]] += 1
        else:
            # 한개 이상 입어야 하니, 입지 않는 경우를 고려하여 2부터 시작
            categories[clothoes[i][1]] = 2

    result = 1
    for key, item in categories.items():
        result *= item

    return result - 1


clothoes = [
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"],
]

solution(clothoes)
