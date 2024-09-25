import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())  # 문서의 개수 n과 궁금한 문서의 위치 m
    priorities = list(map(int, input().split()))  # 중요도 리스트
    queue = deque([(priorities[i], i) for i in range(n)])  # (중요도, 인덱스) 튜플로 큐 생성
    
    count = 0  # 인쇄된 문서 수
    
    while queue:
        current = queue.popleft()  # 큐의 맨 앞 문서
        # 큐에 남아 있는 문서 중 현재 문서보다 중요도가 높은 문서가 있는지 확인
        if any(current[0] < other[0] for other in queue):
            queue.append(current)  # 현재 문서를 큐의 맨 뒤로 보냄
        else:
            count += 1  # 인쇄 수 증가
            if current[1] == m:  # 현재 문서가 우리가 찾는 문서인지 확인
                print(count)  # 인쇄된 순서를 출력
                break


'''
이렇게 푸는게 더 편하다고 생각을 합니다.(참고 코드)
from collections import deque
import sys

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        best = max(queue)  #현재의 최댓값이 가장 먼저 배출되므로 최댓값을 저장
        front = queue.popleft() # 큐의 front를 뽑았으므로
        m -= 1 # 내 위치가 한 칸 당겨진다.

        if best == front: # 뽑은 숫자가 제일 큰 숫자일 때
            count += 1 # 하나가 영원히 배출되므로 순번 하나 추가
            if m < 0: # m이 0이라는 것은 뽑은 숫자가 내 숫자라는 뜻.
                print(count)
                break

        else:   # 뽑은 숫자가 제일 큰 숫자가 아니면
            queue.append(front) # 제일 뒤로 밀려나게 됨
            if m < 0 :  # 제일 앞에서 뽑히면
                m = len(queue) - 1 # 제일 뒤로 이동
'''