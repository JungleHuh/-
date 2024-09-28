
# 보석 - 무게 가격, 가방이 있어서 최대 무게 C, 한개의 보석만 훔
# 약간 그리디 알고리즘 같기도한데...
import heapq
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
jewerly_dict = []
bag_limit = []

for _ in range(n):
    weight, price = map(int, input().split())
    jewerly_dict.append(( weight, price))


for _ in range(k):
    bag_limit.append(int(input()))

jewerly_dict.sort(key=lambda x: x[0])

bag_limit.sort()

max_heap = []
total_value = 0
idx = 0

for bag in bag_limit:
    while idx < n and jewerly_dict[idx][0] <= bag:
        heapq.heappush(max_heap, -jewerly_dict[idx][1])
        idx +=1

    if max_heap:
        total_value += -heapq.heappop(max_heap)

print(total_value)



