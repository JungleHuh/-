import sys
input = sys.stdin.readline
list = []

n = int(input())
for i in range(n):
    list.append(i)

list.sort(reverse= True)
cnt = 0
result = 0

for i in list:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0




