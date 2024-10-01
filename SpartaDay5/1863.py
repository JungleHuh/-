import sys
input = sys.stdin.readline

# 꺾인 선 찾기
n = int(input())
lst = []
for _ in range(n):
    x,y = map(int, input().split())
    lst.append((x,y))
    print(lst)