input_data = input()
row = int(input_data[1])
# a가 나오면 숫자로 변환하고, 거기서 a를 빼주고 1을 더하면, 좌표상 1이됨
# a를 기준으로 b,c,d,e,f,g,h의 좌표가 하나씩 증가해야 함으로, 각 문자열(b,c,d,e,f,g,h)를 숫자로 변환해서 a(기준값)으로 빼주어야 한다.
# 여기서는 문자열을 변환하고, a라는 기준을 중심으로 좌표를 다시 설정하는 것이 포인트
col = int(ord(input_data[0])) - int(ord('a')) + 1

count = 0
steps = [(-2,1), (-2,-1), (2,1), (2,-1), (-1,1),(-1,-1),(1,-1), (1,1)]

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
     

    if 1 <= next_row < 8 and 1<= next_col < 8:
        count +=1
print(count)