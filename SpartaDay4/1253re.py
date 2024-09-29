import sys
input = sys.stdin.readline

n = int(input())  # 입력받은 숫자의 개수
arr = list(map(int, input().split()))  # 숫자 리스트
arr.sort()  # 배열을 정렬하여 투 포인터 알고리즘을 적용하기 쉽게 만듦
count = 0  # 좋은 수의 개수를 셀 변수

# 배열에서 각 숫자가 다른 두 숫자의 합으로 나타나는지 확인
for i in range(n):
    left, right = 0, n - 1  # 투 포인터: 배열의 양 끝에서 시작

    while left < right:
        if left == i:  # i번째 수는 제외하고 확인
            left += 1
            continue
        if right == i:  # i번째 수는 제외하고 확인
            right -= 1
            continue

        total = arr[left] + arr[right]

        if total == arr[i]:  # 두 수의 합이 arr[i]와 같은 경우
            count += 1
            break  # 한 번 찾으면 더 이상 찾지 않고 종료
        elif total < arr[i]:
            left += 1  # 합이 작으면 왼쪽 포인터를 증가시켜 더 큰 수로 만듦
        else:
            right -= 1  # 합이 크면 오른쪽 포인터를 감소시켜 더 작은 수로 만듦

print(count)

#시간 복잡도는 O(n log n) (정렬) + O(n) (투 포인터 탐색) = **O(n log n)