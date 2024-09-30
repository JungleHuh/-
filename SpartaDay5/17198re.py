import sys
from collections import deque
input = sys.stdin.readline

# 10x10 고정 크기 그래프 입력
graph = []
for i in range(10):
    graph.append(list(input().strip()))

# 방향 벡터 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 외양간(B)와 호수(L)의 위치 찾기
barn = None
lake = None
for i in range(10):
    for j in range(10):
        if graph[i][j] == 'B':
            barn = (i, j)
        elif graph[i][j] == 'L':
            lake = (i, j)

def bfs(start, end):
    queue = deque([start])
    visited = [[False] * 10 for _ in range(10)]  # 방문 여부와 거리를 저장
    visited[start[0]][start[1]] = True 

    while queue:
        x, y = queue.popleft()

        # 호수(L)에 도달하면 최단 거리 반환
        if (x, y) == end:
            return visited[x][y] - 1  # 외양간과 호수 인접한 소 제외

        # 4방향으로 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 격자 안에 있고, 빈 공간이며 아직 방문하지 않았다면 이동
            if 0 <= nx < 10 and 0 <= ny < 10 and graph[nx][ny] != 'R' and visited[nx][ny] == False:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return -1  # 경로가 없는 경우

# 외양간에서 호수까지의 최소 경로 찾기
result = bfs(barn, lake)
print(result)
