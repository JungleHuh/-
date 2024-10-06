import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())  # 테스트 케이스 수

for _ in range(tc):
    n = int(input())  # 카드의 개수
    cards = list(input().split())  # 카드 리스트

    result = deque()  # 결과를 담을 덱

    for card in cards:
        # 현재 카드가 현재까지 만든 문자열의 첫 카드보다 작으면 왼쪽에 넣음
        if not result or card <= result[0]:
            result.appendleft(card)  # 왼쪽에 삽입
        else:
            result.append(card)  # 오른쪽에 삽입

    # 최종 결과 출력 (deque를 list로 변환하여 문자열로 출력)
    print(''.join(result))
