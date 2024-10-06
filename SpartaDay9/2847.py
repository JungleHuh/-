import sys
input = sys.stdin.readline

n = int(input())
lst = []
count = 0

# 각 레벨 점수 입력 받기
for _ in range(n):
    lst.append(int(input()))

# 뒤에서부터 탐색하면서 점수를 감소시킴
for i in range(n - 1, 0, -1):
    if lst[i] <= lst[i - 1]:
        count += (lst[i - 1] - lst[i] + 1)  # 차이만큼 감소해야 함
        lst[i - 1] = lst[i] - 1  # 점수가 감소된 상태로 업데이트

print(count)
