import sys
from collections import deque
input = sys.stdin.readline

computer = int(input())  
pair = int(input())  


graph = [[] for _ in range(computer + 1)]  
visited = [0] * (computer + 1)  

#양방향 연결 그래프 구성
for i in range(pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# BFS 
def bfs(graph, r, visited):
    # 시작점(r)을 큐에 넣고 방문 처리
    queue = deque([r])
    visited[r] = 1
    count = 1  # 감염된 컴퓨터 수 (1번 컴퓨터부터 시작하므로 1)

    while queue:
        r = queue.popleft()
        for i in graph[r]:
            if visited[i] == 0:
                visited[i] = 1  
                queue.append(i) 
                bfs(graph, i, visited)

# 1번 컴퓨터에서 시작해 바이러스 전파 탐색
bfs(graph, 1, visited)

# 감염 컴퓨터
worm = 0

for i in visited:
    if i == 1:
        worm += 1

# 1번 컴퓨터는 제외해야 하므로, 감염된 컴퓨터 수에서 1을 뺀 값을 출력
print(worm - 1)
