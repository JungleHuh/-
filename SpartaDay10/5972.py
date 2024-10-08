import sys
import heapq
input = sys.stdin.readline

def djikstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 0,1이 뽑힘
        #최단 거리가 아닐 경우 Skip
        if distance[now] < dist:
            continue
        for v,w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

distance = [1e9] * (n+1)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
djikstra(1)
print(distance[n])

# https://www.youtube.com/watch?v=611B-9zk2o4&t=975s