array = [5, 7, 9, 0, 4, 2, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]  # 피벗은 첫 번째 요소
    tail = array[1:]  # 피벗을 제외한 나머지 리스트

    # 분할: 피벗을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽
    left_side = [x for x in tail if x <= pivot]  # 피벗보다 작거나 같은 값
    right_side = [x for x in tail if x > pivot]  # 피벗보다 큰 값

    # 재귀적으로 왼쪽, 오른쪽 정렬 후 병합
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
