array = [5,7,9,0,4,2,6,2,4,8]

def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    pivot = start # 첫 번째 원소를 피벗(기준)으로 삼음
    left = start + 1 # 옆에 원소와 맨끝의 원소를 비교하는 정렬 방식이니까!
    right = end
    while(left <= right):
        while (left <= end and array[left] <= array[pivot]):
            left +=1 
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
        quick_sort(array, start, right -1)
        quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)