import sys
input = sys.stdin.readline

a,b= map(int, input().split())
result = 0

for _ in range(a):
    data = list(map(int, input().split()))
    min_value = 10001
    for k in data:
        min_value = min(min_value, k)
    result = max(result, min_value)
print(result)

    

