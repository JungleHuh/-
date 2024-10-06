import sys
from collections import deque
input = sys.stdin.readline
 
n,m = map(int, input().split())

graph = [[] for _ in range(m+1)]
visited = [False] * 100001

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

for i in fan_node:
    if visited[i]:
        print('Yes')
        break
    else:
        print('yes')

### 생각해보니까, 아건 BFS로 하면 안되고, DFS로 해야겠다.
# BFS로 한 이유는, 팬_노드가 없는 칸만  찾으면 되겠다고 생각했는데, 문제 이해를 잘못했다.
# DFS로 팬이 없는 칸으로 끝까지 갈 수 있는 경로를 확인하는 것이 문제.
# 큐에 모든 경우의 수 넣고 빼는 BFS로는 경로 추적이 불가능하다.
# DFS로 끝 경로 기록하면서 하는 방식으로 풀어야겠다. 

            
