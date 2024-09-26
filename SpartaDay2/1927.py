import heapq

n = int(input())
heap = []

for i in range(n):
    m = int(input())
    if m != 0:
        heapq.heappush(heap, m)
    else:
        if not heap:
            print(0)
        else:
            k = heapq.heappop()
            print(k)



