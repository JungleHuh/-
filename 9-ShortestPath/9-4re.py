import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    graph[x].append((y,z))

def djikstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]
            # distance[i[0]]은 노드번호(예를 들어 2번)/처음 INF값으로 된 부분 업데이트
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

djikstra(start)

count = 0
max_distacne = 0
for d in distance:
    if d != 1e9:
        count +=1
        max_distacne = max(max_distacne, d)

print(count-1, max_distacne)



