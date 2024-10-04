import sys
from collections import deque

input = sys.stdin.readline

#  방향은 북, 동, 남, 서로 한다
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(r, c, d):
    count = 1  # 처음위치는 무조건 비워져 있음
    queue = deque([(r, c, d)]) # 여기서 튜플로 처리해야되는데, 배열로 처리해서 틀림
    visited[r][c] = True  

    while queue:
        x, y, dir = queue.popleft()
        found = False

        # 4방향 체크
        for i in range(4):
            next_dir = (dir + 3) % 4  # 반시계방향 회전
            next_x = x + dx[next_dir]
            next_y = y + dy[next_dir]

            # 범위를 벗어나지 않으면서 아직 청소되지 않은 빈 칸이 있는 경우
            if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] == 0 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                count += 1
                queue.append((next_x, next_y, next_dir))
                found = True
                break  # 이동했으면 다시 1번으로 돌아감

        # 이동할 수 없는 경우(벽 or 다 True) -> 후진하는 경우의 수
        if not found:
            back_dir = (dir + 2) % 4 # 북 -> 남(+2), 서 -> 동(+2)와 같이 후진 로직
            back_x = x + dx[back_dir]
            back_y = y + dy[back_dir]

            # 후진할 수 있으면 후진
            if 0 <= back_x < n and 0 <= back_y < m and graph[back_x][back_y] == 0:
                queue.append((back_x, back_y, dir))
            else:
                # 후진도 할 수 없으면 작동 멈춤
                break

    return count

n, m = map(int, input().split())  
r, c, d = map(int, input().split()) 
graph = [list(map(int, input().split())) for _ in range(n)] 
visited = [[False] * m for _ in range(n)] 

result = bfs(r, c, d)
print(result)
