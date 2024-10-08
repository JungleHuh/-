import sys
input = sys.stdin.readline

graph = [list(map(int, input().rstrip().split())) for _ in range(5)]
answer =[list(map(int, input().rstrip().split())) for _ in range(5)]
bingo = [[0] * 5 for _ in range(5)]

def row():
    ans = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[i][j] == 1:
                cnt +=1 
            if cnt == 5:
                ans +=1
    return ans

def col():
    ans = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if bingo[j][i] == 1:
                cnt +=1
            if cnt == 5:
                ans +=1
    return ans

def check():
    ans = 0
    cnt = 0
    for I in range(5):
        if bingo[i][5-i-1] ==1 :
            cnt +=1
    if cnt ==5:
        ans +=1
    cnt = 0
    for i in range(5):
        if bingo[i][i] == 1:
            cnt +=1
    if cnt == 5:
        ans +=1
    return ans

cnt = 0
for i in range(5):
    for  j in range(5):
        



