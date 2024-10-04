import sys
from collections import deque
input = sys.stdin.readline

# 로봇 청소기가 회전할 때 방향을 설정 (북, 동, 남, 서) 
# 반시계방향으로 회전하기 위해 0: 북, 1: 동, 2: 남, 3: 서로 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 후진 방향 설정 (0: 북, 1: 동, 2: 남, 3: 서)
back_dx = [1, 0, -1, 0]
back_dy = [0, -1, 0, 1]

def bfs(r, c, d):
    count = 0  # 청소한 칸의 수
    queue = deque([(r, c, d)])  # 시작 위치와 방향
    visited[r][c] = True  # 시작 위치 청소
    count += 1

    while queue:
        x, y, direction = queue.popleft()
        found_cleanable = False
        
        for i in range(4):
            # 반시계 방향으로 회전하며 탐색 (현재 방향 기준 반시계로 한 칸씩 돌아감)
            nd = (direction + 3 - i) % 4
            nx, ny = x + dx[nd], y + dy[nd]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, nd))
                count += 1
                found_cleanable = True
                break
        
        # 만약 청소할 곳을 못 찾았으면 후진 시도
        if not found_cleanable:
            back_x = x + back_dx[direction]
            back_y = y + back_dy[direction]
            if graph[back_x][back_y] == 0:  # 후진할 곳이 빈 칸이면
                queue.append((back_x, back_y, direction))
            else:  # 벽이라 후진 못 하면 종료
                break

    return count

# 입력 받기
n, m = map(int, input().split())  # 방 크기
r, c, d = map(int, input().split())  # 시작 위치와 방향
graph = [list(map(int, input().split())) for _ in range(n)]  # 방 상태
visited = [[False] * m for _ in range(n)]  # 청소 여부 기록

# 로봇 청소기 시작
result = bfs(r, c, d)
print(result)
