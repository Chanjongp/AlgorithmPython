LEFT = 0
MID = 1
RIGHT = 2


def solution(n):
    # 각 행마다 도는 횟수
    turn_limit = n - 1
    # dir이 0,1,2 -> 왼쪽변, 밑변, 오른쪽변 (올라감)
    dir, cnt = LEFT, 1
    # 삼각형 높이 및 pos
    pos = [1, 1]

    # Intialize
    # 안으로 들어갈 때마다 카운트해주는 변수
    inside_cnt = 0
    size = 0
    for i in range(1, n + 1):
        size += i
    data = [0] * (size + 1)

    # Logic
    for i in range(1, size + 1):
        data[pos[1]] = i

        # pos 어디로 갈지 정의 (왼, 중, 오)
        if dir == 0:
            pos[1] += pos[0]
            pos[0] += 1
        elif dir == 1:
            pos[1] += 1
        elif dir == 2:
            pos[1] -= pos[0]
            pos[0] -= 1

        # cnt가 turn_limit보다 커지면
        if cnt == turn_limit:
            dir += 1
            cnt = 1
        # 아니면 cnt 1 추가
        else:
            cnt += 1

        # dir가 3번이나 돌았으면 하위 삼각형으로 접근
        if dir == 3:
            turn_limit -= 3
            inside_cnt += 1
            pos[0] += 2
            pos[1] += 4 * inside_cnt

            dir = 0

    return data[1:]
