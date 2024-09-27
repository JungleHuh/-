import sys
sys.setrecursionlimit(10000)  # 재귀 한도를 늘립니다.
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())  
graph = []
visited = [[False] * c for _ in range(r)]  # 방문 체크 배열

for _ in range(r):
    graph.append(list(input().rstrip()))

result_v = 0  # 전체 늑대(v) 수
result_k = 0  # 전체 양(k) 수

# DFS 함수
def dfs(x, y):
    dx = [0,0,-1,1]
    dy = [-1, 1, 0, 0]
    count_v = 0  # 각 영역 내 늑대 수
    count_k = 0  # 각 영역 내 양 수
    
    stack = [(x, y)]  # DFS를 위한 스택
    if graph[x][y] == 'v':
        count_v += 1
    elif graph[x][y] == 'k':
        count_k += 1
    visited[x][y] = True  # 방문 체크

    # 스택을 사용한 DFS 구현
    while stack:
        cx, cy = stack.pop()
        
        for i in range(4):
            next_x = cx + dx[i]
            next_y = cy + dy[i]

            if 0 <= next_x < r and 0 <= next_y < c and not visited[next_x][next_y] and graph[next_x][next_y] != '#':
                visited[next_x][next_y] = True
                stack.append((next_x, next_y))
                
                if graph[next_x][next_y] == 'v':
                    count_v += 1
                elif graph[next_x][next_y] == 'k':
                    count_k += 1
    
    # 양과 늑대 수 비교 후 결과 갱신
    global result_v, result_k
    if count_v >= count_k:
        result_v += count_v  # 늑대가 더 많으면 늑대만 살아남음
    else:
        result_k += count_k  # 양이 더 많으면 양만 살아남음

# 탐색 시작!
for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != '#':
            dfs(i, j)

print(result_k, result_v)
