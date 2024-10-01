import sys
from collections import deque
input = sys.stdin.readline
 
n,m = map(int, input().split())

graph = [[] for _ in range(m+1)]
visited = [False] * 10

# 사이클이 없드아..!
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

fan = int(input())
fan_node = list(map(int, input().strip().split()))

def bfs(graph, R, visited):
    queue = deque([R])
    visited[R] = 1
    
    while queue:
        R = queue.popleft()
        for i in graph[R]:
            if visited[i] == False:
                visited[i] = True
                queue.append(i)
                bfs(graph, i, visited)
# 여기서 Visited값이 True로 바뀐 것들 중에 fan_node와 만나는 점들이 있으면 'YES' 아니면 'yes'

bfs(graph, 1, visited)

for i in range(1, n+1):
    if visited[i]


            
