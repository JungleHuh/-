import sys
input = sys.stdin.readline

n = int(input())

# 2와 5만 거스름
# 동전 개수 최소
# n 일 떄 최소 동전 개수
count = 0
while True:
    
    if n % 5 == 0:
        n = n/5
        count += n//5
        break
    n -= 2
    count += 1

if n < 0:
    print(-1)
else:
    print(count)
        