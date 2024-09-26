import heapq

n = int(input())
heap = []

for i in range(n):
    present = input().split()
    if present[0] == '0' and not heap:
        print(-1)
    elif present[0] != '0':
        for i in range(int(present[0])):
            heapq.heappush(heap, -int((present[i+1])))
    else:
        given_present = heapq.heappop(heap)
        print(-given_present)