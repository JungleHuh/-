import sys
input = sys.stdin.readline

# 꺾인 선 찾기 문제인 것 같음
n = int(input())
lst = []

for _ in range(n):
    x,y = map(int, input().split())
    lst.append((x,y))

# 일단 Sort는 해주자. 그러면 y값만 비교하면 된다. 그리고 1에서 시작하니까 Count 1 해주고.
lst.sort()
count = 1
for i in range(n):
    
    
