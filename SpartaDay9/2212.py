import sys
input = sys.stdin.readline

n = int(input())
c = int(input())
dist = []

censor = list(map(int, input().strip().split()))
censor.sort()

if c >= n:
    print(0)
    exit()

for i in range(1,n):
    dist.append(censor[i]-censor[i-1])

dist.sort(reverse=True)

for i in range(c-1):
    dist.pop(0)

print(sum(dist))



