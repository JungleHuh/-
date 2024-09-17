def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

N = int(input())
array = list(map(int, input().split()))
array.sort()

M = int(input())
Buys = list(map(int, input().split()))

for Buy in Buys:
    # 여기서 인덱스를 파라미터로 넣어주는게 약간 헷갈림
    result = binary_search(array, Buy, 0, N-1)
    
    if result != None:
        print('yes', end = ' ')
    else:
        print("no", end = " ")
