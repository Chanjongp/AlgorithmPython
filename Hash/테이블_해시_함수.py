def solution(data, col, row_begin, row_end):
    answer = []
    result = 0
    # 2. col번째 컬럼 정렬
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    for i, row in enumerate(data[row_begin-1:row_end], start=row_begin):
        # 3. S_i 나머지 합 정의
        s_i = sum([j % i for j in row])
        answer.append(s_i)

    for i in answer:
        result = result ^ i
    
    return result