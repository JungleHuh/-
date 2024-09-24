# 문제를 잘 읽자 -> 그래야 코드가 이해가 된다.
import sys
input = sys.stdin.readline

data = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result +=1
        count = 0

print(result)



