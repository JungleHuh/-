import sys
input = sys.stdin.readline

n  = int(input())
arr = list(map(int, input().split()))
good = set()
count = 0

for i in range(n):
    for j in range(i,n-1):
        k = arr[i] + arr[j+1] 
        if k in arr:
            good.add(k)
for i in good:
    count +=1
print(count)

