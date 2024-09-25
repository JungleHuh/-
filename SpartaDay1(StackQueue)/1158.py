import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(range(1, n + 1))
done = []

# Josephus problem 해결
while queue:
    queue.rotate(-k + 1)  # 왼쪽으로 k-1만큼 회전
    done.append(queue.popleft())  # 맨 앞의 요소를 제거하고 결과에 저장

# 원하는 형식으로 출력
print(f"<{', '.join(map(str, done))}>")
