import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v,e,r = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [0]* (v+1)

cnt = 1

def dfs(graph, start, visited):
    global cnt
    visited[start] = cnt

    for i in graph[start]:
        if visited[i] == 0:
            cnt +=1
            dfs(graph, i, visited)

for i in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(v+1):
    graph[i].sort()

dfs(graph, r, visited)

for i in range(1,v+1):
    print(visited[i])

    


