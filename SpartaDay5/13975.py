import sys
input = sys.stdin.readline

tc = int(input())  # 테스트 케이스의 수 입력

# 각 테스트 케이스에 대해 수행
for _ in range(tc):
    k = int(input())  # 리스트의 길이 입력
    lst = list(map(int, input().strip().split()))  # 리스트 입력
    
    lst.sort()  # 리스트를 오름차순 정렬
    total_sum = 0  # 전체 합을 저장할 변수
    result_list = []  # 더한 값들을 저장할 리스트
    
    # 처음과 끝을 차례대로 더해나감
    left = 0  # 처음 인덱스
    right = k - 1  # 끝 인덱스

    while left < right:
        # 처음과 끝값을 더하고 저장
        current_sum = lst[left] + lst[right]
        total_sum += current_sum
        result_list.append(current_sum)  # 중간 계산 결과 저장
        left += 1  # 처음 인덱스 증가
        right -= 1  # 끝 인덱스 감소

    # 만약 리스트가 홀수 길이라면, 중간에 남은 값 더하기
    if left == right:
        total_sum += lst[left]
        result_list.append(lst[left])  # 마지막 남은 값 저장

    # 더해진 값들의 리스트 출력
    print("더한 값들:", result_list)
    # 전체 합 출력
    print("전체 합:", total_sum)
