import sys
import bisect

input = sys.stdin.readline

n, m = map(int, input().split())  # n: target 리스트 크기, m: 구간(line) 개수
target = list(map(int, input().strip().split()))  # target 리스트
target.sort()  # 이진 탐색을 위해 미리 정렬

# 구간(line) 처리
for _ in range(m):
    a, b = map(int, input().split())  # 구간의 시작과 끝

    # 이진 탐색을 통해 구간에 속하는 target 값의 개수 계산
    left_idx = bisect.bisect_left(target, a)  # 구간 시작(a) 이상인 첫 위치
    right_idx = bisect.bisect_right(target, b)  # 구간 끝(b) 이하인 마지막 위치

    # 구간에 속하는 target 요소의 개수는 right_idx - left_idx
    print(right_idx - left_idx)
