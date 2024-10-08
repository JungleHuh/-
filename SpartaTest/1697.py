n, k = map(int, input().split())
distacne = n-k
# 왠지 그리디 같음

def bfs(x):
    if x <= distacne//2:
        x =  2*x
    elif x > distacne//2:
        x = x-1