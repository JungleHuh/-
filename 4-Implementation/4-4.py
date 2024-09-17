#게임개발 p.118 어렵네.
import sys
input = sys.stdin.readline

row,col = map(int, input().split())

x,y,direction = map(int, input().split())
#row과 col로 board를 만들 떄는, col이 가로로 가고, row가 세로로 증가함.
board = [[0]* col for _ in range(row)]
board[x][y] = 1

array = []
#이 반복문을 세로로 증가하니 row로 받아줘야겠지.
for i in range(row):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
dir = [0,1,2,3]
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if board[nx][ny] == 0 and array[nx][ny] == 0:
        board[nx][ny] = 1
        x = nx 
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)


