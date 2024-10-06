import sys
import heapq
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    num, start, end = map(int, input().split())
    lst.append((num,start,end))

lst.sort(key = lambda x: x[1])

classroom = []

for _, start, end in lst:
    if classroom and classroom[0] <= start:
        heapq.heappop(classroom)
    heapq.heappush(classroom, end)

print(len(classroom))


