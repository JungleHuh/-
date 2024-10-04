import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().strip().split()))
dp = [0]*(n+1)

for i in range(n):
    for j in range(0,i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp)+1)