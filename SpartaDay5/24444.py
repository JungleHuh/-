from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]* (N+1)

for i in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, R, visited):
    queue = deque([R])
    visited[R] = 1
    count = 1

    while queue:
        R = queue.popleft()
        for i in graph[R]:
            if visited[i] == 0:
                queue.append(i)
                count +=1
                visited[i] = count
    return count
    
for i in range(N+1):
    graph[i].sort() 

bfs(graph, R, visited)

for i in visited[1::]:
    print(i)   
