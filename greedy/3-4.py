import sys
input = sys.stdin.readline

a,b = map(int, input().split())
cnt = 0
while a > 1:
    if a % b == 0:
        cnt += 1
        a = a//b
    else:
        cnt += 1
        a - 1
        a = a -1
print(cnt)
