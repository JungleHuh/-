import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
sum_lst = sum(lst)
print(sum_lst)

for i in range(1,sum_lst+1):
    if i in combination_lst
import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())  # 리스트 크기
lst = list(map(int, input().split()))  # 리스트 입력

# 리스트를 오름차순으로 정렬
lst.sort()

# 구할 수 없는 가장 작은 값을 찾기 위한 초기값
smallest_unreachable = 1

# 리스트의 값을 하나씩 더해가면서 만들 수 있는 범위를 확장
for num in lst:
    if num > smallest_unreachable:
        # 만약 현재 숫자가 현재까지 만들 수 있는 범위를 넘어가면 그 값이 구할 수 없는 값임
        break
    smallest_unreachable += num

# 결과 출력
print(smallest_unreachable)

# https://aerocode.net/392

9 + 9.5 + 7 + 3.5 = 29