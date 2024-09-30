import sys
input = sys.stdin.readline

# 이분 탐색으로 구간 내 시작점 찾기 (이상)
def lower_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            right = mid
        else:
            left = mid + 1
    return left

# 이분 탐색으로 구간 내 끝점 찾기 (이하)
def upper_bound(arr, x):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > x:
            right = mid
        else:
            left = mid + 1
    return left


n, m = map(int, input().split()) 
target = list(map(int, input().strip().split()))
line = [tuple(map(int, input().split())) for _ in range(m)]

# 이분 탐색을 위한 target 리스트 정렬
target.sort()

# 구간(line)에 속하는 target 값 찾기
for a, b in line:
    # a 이상인 첫 번째 위치 찾기
    start_idx = lower_bound(target, a)
    # b 이하인 마지막 위치 찾기
    end_idx = upper_bound(target, b)

    # 구간 내 target 값 개수는 end_idx - start_idx
    print(end_idx - start_idx)
