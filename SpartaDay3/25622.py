import sys
sys.setrecursionlimit(1000000)

def dfs(node, parent):
    size = 1
    children = []
    for child in graph[node]:
        if child != parent:
            child_size, child_groups = dfs(child, node)
            size += child_size
            children.extend(child_groups)
    
    if size % 3 == 0:
        if size == 3:
            return size, [[node] + [child for child in graph[node] if child != parent]]
        else:
            return size, children + [[node] + [child for child in graph[node] if child != parent][:2]]
    
    return size, children

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

total_size, groups = dfs(1, 1)

if total_size == N and len(groups) * 3 == N:
    print("S")
    for group in groups:
        print(*group)  # 수정된 부분: sorting 제거
else:
    print("U")