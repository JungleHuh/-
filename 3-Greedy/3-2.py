import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
fisrt = data[a-1]
second = data[a-2]

count = int(b/(c+1))*c
count += b % (c+1)

result = 0
result += (count) * fisrt
result += (b-count) * second

print(result)

