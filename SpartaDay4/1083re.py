def maximize_array(arr, S):
    n = len(arr)
    
    # 남은 스왑 횟수를 추적합니다.
    swaps_left = S

    # 배열을 순차적으로 확인하면서, 가능한 가장 큰 값을 앞으로 이동시킵니다.
    for i in range(n):
        if swaps_left <= 0:
            break
        
        # 현재 위치에서부터 swaps_left 범위 내에서 가장 큰 값을 찾아야 합니다.
        max_idx = i
        for j in range(i + 1, min(i + swaps_left + 1, n)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        
        # max_idx에 있는 가장 큰 값을 앞으로 이동시키기 위해 스왑합니다.
        for j in range(max_idx, i, -1):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        
        # 사용한 스왑 횟수를 차감합니다.
        swaps_left -= (max_idx - i)

    return arr

# 입력 처리
N = int(input())  # 배열의 크기
arr = list(map(int, input().split()))  # 배열 A
S = int(input())  # 최대 스왑 가능 횟수

# 사전순으로 가장 뒤에 오는 배열 만들기
result = maximize_array(arr, S)

# 결과 출력
print(*result)
