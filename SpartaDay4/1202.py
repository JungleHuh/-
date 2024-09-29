import heapq  
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) 
jewelry_dict = [] 
bag_limit = [] 

for _ in range(n):
    weight, price = map(int, input().split())  # 각 보석의 무게와 가격 입력
    jewelry_dict.append((weight, price)) 

for _ in range(k):
    bag_limit.append(int(input())) 

# 보석을 무게 기준으로 오름차순 정렬
jewelry_dict.sort(key=lambda x: x[0]) 

# 가방을 최대 무게 기준으로 오름차순 정렬
bag_limit.sort()  

max_heap = [] 
total_value = 0  # 훔친 보석의 총 가치=
idx = 0 

# 각 가방에 대해 보석을 넣을 수 있는지 확인
for bag in bag_limit:
    # 현재 가방의 무게를 초과하지 않는 모든 보석을 최대 힙에 추가
    while idx < n and jewelry_dict[idx][0] <= bag:
        heapq.heappush(max_heap, -jewelry_dict[idx][1])
        idx += 1

    if max_heap:
        total_value += -heapq.heappop(max_heap)

print(total_value)
