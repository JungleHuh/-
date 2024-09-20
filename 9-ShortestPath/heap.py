# 최소 힙(파이썬은 Min_heap이 기본: 낮은데이터부터 꺼내짐: 오름차순 정렬)
import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)
    
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result 

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)