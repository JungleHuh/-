import sys
import heapq

input = sys.stdin.readline

# 입력 받기
N, H, T = map(int, input().split())
heap = []

# 거인들의 키를 최대 힙으로 저장 (음수로 변환해서 사용)
for _ in range(N):
    H = int(input())
    heapq.heappush(heap, -H)  # 최대 힙으로 사용하기 위해 음수로 삽입

count = 0  # 뿅망치 사용 횟수

# 가장 큰 거인부터 키를 줄이기 시작
while count < T:
    largest = -heapq.heappop(heap)  # 최대 힙에서 가장 큰 값을 가져옴 (양수로 변환)
    
    if largest < H:
        # 이미 센티보다 작으면 더 이상 할 필요 없음
        break
    
    if largest == 1:
        # 키가 1인 경우 더 이상 줄일 수 없으므로 처리 종료
        heapq.heappush(heap, -largest)
        break
    
    # 키를 절반으로 줄이기
    new_height = largest // 2
    heapq.heappush(heap, -new_height)  # 다시 힙에 삽입 (음수로 삽입)
    
    count += 1  # 뿅망치 사용 횟수 증가

# 뿅망치 사용 후 가장 큰 거인 확인
largest_remaining = -heap[0]

if largest_remaining < H:
    # 모든 거인이 센티보다 작아진 경우
    print("YES")
    print(count)
else:
    # 아직 센티보다 큰 거인이 남아있는 경우
    print("NO")
    print(largest_remaining)
