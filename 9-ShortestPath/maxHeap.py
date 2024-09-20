# 최대힙 -> Value를 음수값으로 넣고, 뺄 때 다시 음수값 붙여주어 최대힙 구현
import heapq

def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)
    
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result 

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)