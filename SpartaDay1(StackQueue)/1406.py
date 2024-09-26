import sys
from collections import deque
input = sys.stdin.readline

str = input()
n = int(input())

queue = deque()

for i in range(n):
    k = input().split()
    command = k[0]
    if command == 'P':
        str.append(k[1])
    elif command == 'L':
        str.rotate(-1)
    elif command == 'D':
        str.rotate(1)
    else:
        if 

