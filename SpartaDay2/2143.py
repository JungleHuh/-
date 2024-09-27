import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수
n = int(input())  # A 리스트의 크기
A = list(map(int, input().strip().split()))  # A 리스트
m = int(input())  # B 리스트의 크기
B = list(map(int, input().strip().split()))  # B 리스트

combination_dict = defaultdict(list)  # defaultdict을 사용해 리스트 값을 저장할 수 있게 함

# A 리스트의 각 값을 개별 키로 분류하여 저장
for i in range(n):
    combination_dict[f'A_{i}'] = A[i]  # A의 인덱스를 포함한 키에 값 추가

# B 리스트의 각 값을 개별 키로 분류하여 저장
for j in range(m):
    combination_dict[f'B_{j}'] = B[j]  # B의 인덱스를 포함한 키에 값 추가

# 출력 확인
print(combination_dict)
