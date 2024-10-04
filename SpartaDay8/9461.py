import sys
input = sys.stdin.readline

tc = int(input())
dp = [0]*101

dp[1], dp[2], dp[3], dp[4], dp[5] = 1,1,1,2,2
for _ in range(tc):
    n = int(input())
    for i in range(1,n+1):
        if i > 5:
            dp[i] = dp[i-2] + dp[i-3]
    print(dp[n])

