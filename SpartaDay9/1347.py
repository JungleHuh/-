import sys
import heapq
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    num, start, end = map(int, input().split())
    lst.append((num,start,end))

lst.sort(key = lambda x: x[1])

class = []

for _. start, end, in lst:
    if class and class[0] <= start:
        heapq.heappop(class)
    heapq.heappush(class, end)

print(len(class))


