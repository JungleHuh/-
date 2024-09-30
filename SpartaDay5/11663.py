import sys
input = sys.stdin.readline

n,m = map(int, input().split())
target = list(map(int, input().strip().split()))
line = []
for i in range(m):
    a,b = map(int, input().split())
    line.append((a,b))

for i in line:
    sum = 0
    start, end = i[0], i[1]
    for spot in target:
        if i[0] <= spot <= i[1]:
            sum +=1
    print(sum)