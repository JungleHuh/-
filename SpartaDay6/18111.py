import sys
input = sys.stdin.readline

n,m,b = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 구현
for _ in range(n):
    