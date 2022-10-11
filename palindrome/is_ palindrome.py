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

if __name__ == "__main__":
    n = 100011
    print(is_palindrome(n))
    