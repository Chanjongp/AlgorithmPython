"""
홍준 -> 자연수 N개

명우에게 질문 M개

첫째줄 -> N (1 ~ N)
둘째줄 -> 칠판에 적은 수 N개 실제 숫자
셋째줄 -> 질문의 갯수 (M)

넷째줄 -> S, E가 한개씩 주어짐
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
"""
import sys

def make_num(question):
    num = 0
    for i in question:
        num = (num * 10) + i
    return num
    

def is_palindrome(num_arr, s, e):
    question = num_arr[s-1:e]
    num = make_num(question)
    num_cp = num

    reverse = 0
    while num_cp:
        # 끝자리 수 가져옴
        last = num_cp % 10
        
        # ex. 16461에서, 1 -> 16으로 갈 때
        # (1 * 10) + 6 = 16
        reverse = (reverse * 10) + last

        num_cp //= 10

    if num == reverse:
        return 1
    else:
        return 0


N = int(sys.stdin.readline())
num_arr = list(map(int, sys.stdin.readline().split()))
M = int(input())
result = []
for _ in range(M):
    s, e = list(map(int, sys.stdin.readline().split()))
    result.append(is_palindrome(num_arr, s, e))


[print(r) for r in result]
    
    