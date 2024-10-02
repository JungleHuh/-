import sys
input = sys.stdin.readline

def is_palindrome(s):
    return s == s[::-1]

def check_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # 한 문자를 제거하고 회문인지 확인
            if is_palindrome(s[left:right]) or is_palindrome(s[left+1:right+1]):
                return 1  # 유사 회문
            else:
                return 2  # 회문이 아님
        left += 1
        right -= 1
    return 0  # 완전 회문

n = int(input())  # 입력 개수
lst = [input().strip() for _ in range(n)]  # 문자열 입력

for s in lst:
    print(check_palindrome(s))  # 각 문자열에 대해 결과 출력
