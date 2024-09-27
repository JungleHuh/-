import sys
input = sys.stdin.readline

r,c = map(int, input().rstrip().split())
graph = []
result_v = 0
result_k = 0
for i in range(6):
    graph.append(list(input().rstrip()))

def dfs(x,y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    count_v = 0
    count_k = 0
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if next_x >0 or next_x <= 6 or next_y >0 or next_y <=6:
            if graph[next_x][next_y] == 'v':
                count_v +=1
            elif graph[next_x][next_y] == 'k':
                count_k +=1
            dfs(next_x, next_y)
    if count_v >= count_k:
        result_v += count_v
        count_k = 0
        result_v += count_v
    else:
        result_k += count_k
        count_v = 0
        result_k += count_k

for i in range(6):
    for j in range(6):
        dfs(i,j)
print(result_v, ' ', result_k)




