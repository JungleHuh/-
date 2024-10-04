import sys
input = sys.stdin.readline

# 입력 처리
n = int(input())
lst = list(map(int, input().strip().split()))

# dp[i]: i번째 수를 마지막으로 하는 증가하는 부분 수열의 최대 합
dp = lst[:]  # 처음에는 각 원소 자체가 최대 합으로 초기화

# 증가하는 부분 수열의 합을 구하는 과정
for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + lst[i])

# dp 배열에서 가장 큰 값이 답
print(max(dp))
