"""
회문인지 확인하는 함수 (숫자)
놓친 포인트: 첫번째 숫자를 어떻게 가져올지 헷갈렸음 
    -> 0으로 초기화해서 시작하면, 10을 곱해도 0으로 되고, 마지막 숫자 첫번쨰로 가져올 수 있음

1. while문
    - 맨 끝자리 하나씩 가져옴 -> %10 하면 나머지로 가져올 수 있음
    - 첫번째부터 숫자 가져와서, 다음 자리에 더함 ()
        ex. 46164일 때
        while문
            첫번째: 4
            두번째: (4 * 10) + 6
            세번째: (46 * 10) + 1
            ...
    - 맨 끝자리 버리고 다시 while문


2. 재귀
"""

def is_palindrome(num):
    # 46164
    left, right = 0, 0

    target = num
    # 0이 될 때까지 회문
    while num:
        # 맨 끝자리 가져옴 -> 4, 6, 1, 6, 4
        right = num % 10
        
        # 첫번째서부터 숫자 가져옴 -> 4, 46, 461, 4616, 46164
        left = (left * 10) + right
        
        num //= 10
    
    return left == target


def reverse(num, rev=0):
    if num == 0:
        return rev
    # 끝자리 가져옴
    right = num % 10

    # 앞자리 에 끝자리 값 추가 -> rev:4 -> (4 * 10) + 6
    rev = (rev * 10) + right
    return reverse(num // 10, rev)


def re_is_palindrome(num):
    return num == reverse(num)

if __name__ == "__main__":
    n = 1001
    print(is_palindrome(n))
    print(re_is_palindrome(n))


    