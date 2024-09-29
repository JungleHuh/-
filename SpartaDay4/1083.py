n = int(input())
arr = list(map(int, input().split()))  # 배열 입력
s = int(input())  # 최대 스왑 횟수
count = 0  # 스왑한 횟수
i = 0  # 배열의 인덱스를 직접 관리

# 최대 s번 스왑이 일어날 수 있음
while i < n - 1 and count < s:
    if arr[i] < arr[i + 1]:
        # 스왑
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        count += 1
        i = 0  # 스왑이 발생하면 다시 처음부터 검사
    else:
        i += 1  # 스왑이 없으면 다음 인덱스로 이동

# 배열 출력
print(*arr)
