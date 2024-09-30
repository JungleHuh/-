import sys
from collections import deque
input = sys.stdin.readline

computer = int(input())
pair = int(input())
graph = [[] for _ in range(computer+1)]
visited = [0]*(computer+1)

for i in range(pair):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, r, visited):
    queue = deque([r])
    visited[r] = 1
    count = 1

    while queue:
        r = queue.popleft()
        for i in graph[r]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                bfs(graph, i, visited)

bfs(graph, 1, visited)

worm = 0

for i in visited:
    if i == 1:
        worm +=1
print(worm -1)



