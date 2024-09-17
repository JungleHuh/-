n = int(input())
directions = input().split()

x = 1
y = 1
direction_x = [-1,1,0,0]
direction_y = [0,0,-1,1]
plans = ['U','D','L','R']

for direction in directions:
    for i in range(len(plans)):
        if direction == plans[i]:
            next_x = x + direction_x[i]
            next_y = y + direction_y[i]
    if next_x < 1 or next_y < 1 or next_x > n or next_y > n:
        continue
    x = next_x
    y = next_y
print(x,y)
