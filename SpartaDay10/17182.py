import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [0]*n
visited[m] = 1
result = sys.maxsize

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 백트래킹 + DFS
def find(cur_node, total, depth):
    global result
    if depth == n:
        result = min(result, total)
        return 
    # 현재까지의 총 비용이 결과보다 크면 가지치기
    if total > result:
        return
    # DFS
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        find(i, total+ graph[cur_node][i], depth +1)
        # 백트래킹 위함
        visited[i] = 0
    
find(m,0,1)
print(result)
