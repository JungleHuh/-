import sys
from collections import deque
input = sys.stdin.readline

graph = []
for i in range(10):
    graph.append(list(map(str, input().strip())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
visited = [0]* 1000000

barn = None
lake = None
# 그래프가 주어졌지, 그러면 어떻게 해야하나. 오히려 좋아!

for i in range(10):
    for j in range(10):
        if graph[i][j] == 'B':
            barn = (i, j)
        elif graph[i][j] == 'L':
            lake = (i, j)

def bfs(start, end):
    queue = deque([start])

    