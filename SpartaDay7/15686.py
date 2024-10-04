import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = []
home = []
chicken = []

for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(n):
        if graph[i][j] == 1:
            home.append((i,j))
        elif graph[i][j] == 2:
            chicken.append((i,j))
visited = [False] * len(chicken)

def dfs(idx, cnt):
    global min_ans

    if cnt == m:

        ans = 0
        for i in home:
            distance = 99999999
            for j in range(len(visited)):



