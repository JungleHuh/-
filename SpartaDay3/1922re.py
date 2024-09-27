# 유니온 파인드(Union-Find) 함수 정의
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
            if rank[root_a] == rank[root_b]:
                rank[root_b] += 1

# 입력 받기
n = int(input())  # 컴퓨터(정점)의 수
m = int(input())  # 연결 가능한 선(간선)의 수

edges = []

# 간선 정보 입력
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선 비용 순으로 오름차순 정렬
edges.sort()

# 유니온 파인드를 위한 초기화
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

# 최소 신장 트리 비용 계산
total_cost = 0
edge_count = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):  # 사이클이 발생하지 않을 때만
        union(parent, rank, a, b)
        total_cost += cost
        edge_count += 1
        if edge_count == n - 1:  # 모든 컴퓨터가 연결되었으면 종료
            break

print(total_cost)
