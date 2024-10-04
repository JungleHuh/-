import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

up_dp = [1]* n
down_dp = [1]* n
up = []
down = []

# 이진탐색으로 Left와 Right 탐색범위 좁히면서 최댓값 찾아보자.
for i in range(n):
    # Bisect_left로 삽입할 왼쪽 인덱스 찾기
    pos = bisect_left(up, lst[i])
    if pos < len(up):
        up[pos] = lst[i]
    else:
        up.append(lst[i])
    up_dp[i] = pos + 1

for i in range(n-1,-1,-1):
    # Bisect_left로 삽입할 왼쪽 인덱스 찾기
    pos = bisect_left(down, lst[i])
    if pos < len(down):
        down[pos] = lst[i]
    else:
        down.append(lst[i])
    down_dp[i] = pos +1

length = 0

for i in range(n):
    length = max(length, up_dp[i] + down_dp[i] -1)

print(length)
