import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
visited = [[0]*(n+1) for _ in range(n+1)]

def djikstra():
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    heap = []
    heapq.heappush(heap, [0,0,0])
    visited[0][0] = 1
    while heap:
        c,x,y = heapq.heappop(heap)

        if (x,y) == (n-1, n-1):
            print(c)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    heapq.heappush(heap, [c + 1, nx, ny])
                else:
                    heapq.heappush(heap, [c, nx, ny])

djikstra()
