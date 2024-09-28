import sys
input = sys.stdin.readline
tc = int(input())

for _ in range(tc):
    n = int(input())
    rank = []
    for _ in range(n):
        a, b = map(int, input().split())
        rank.append((a,b))
    rank.sort(key = lambda x: x[1])
    min = rank[0][0]

    count = 1
    for i in range(n):
        if rank[i][0] < min:
            min = rank[i][0]
            count += 1
    print(count)



