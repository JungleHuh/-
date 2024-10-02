import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    index,value = q.popleft()
    ans.append(index +1)

    if value > 0:
        q.rotate(-(value -1))
    elif value < 0:
        q.rotate(-value)
print(' '.join(map(str, ans)))


