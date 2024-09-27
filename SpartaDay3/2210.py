import sys
input = sys.stdin.readline

def dfs(x, y, limit):
    if len(limit) == 6:
        result.add(limit)  # 중복 없이 저장하기 위해 리스트 대신 집합 사용
        return

    # 이동 방향: 상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        # 격자 범위를 벗어나지 않도록 체크
        if 0 <= next_x < 5 and 0 <= next_y < 5:
            dfs(next_x, next_y, limit + str(graph[next_x][next_y]))  # 정수를 문자열로 변환하여 추가

# 입력 받기
graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))

result = set()  # 중복을 방지하기 위해 집합 사용

# 각 좌표에서 DFS 시작
for i in range(5):
    for j in range(5):
        dfs(i, j, str(graph[i][j]))  # 시작 값도 문자열로 변환하여 전달

# 결과 출력: 중복 없는 6자리 숫자 조합의 개수
print(len(result))
