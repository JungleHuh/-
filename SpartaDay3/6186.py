from collections import deque

r,c = map(int, input().split())
graph = []
visited = [[False]*c for _ in range(r)]

for i in range(c):
    graph.append(list(input()))

def bfs(x,y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    if nx >= 0 and nx < 6 and ny >=0 and ny <6:
        


            
        

