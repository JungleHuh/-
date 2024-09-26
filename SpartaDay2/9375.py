import sys
from collections import defaultdict

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    accessory_dict = defaultdict(list)
    
    # 아이템을 카테고리별로 저장
    for _ in range(n):
        item, category = input().strip().split()
        accessory_dict[category].append(item)
    
    result = 1
    
    # 각 카테고리에서 선택할 수 있는 경우의 수 계산
    for category in accessory_dict:
        result *= (len(accessory_dict[category]) + 1)  # 아이템을 고르지 않는 경우 포함
        
    # 모든 카테고리에서 아무것도 고르지 않는 경우 하나 빼기
    print(result - 1)

'''
import sys
from collections import defaultdict

input = sys.stdin.readline

tc = int(input())  # 테스트 케이스 수
accessory_dict = defaultdict(list)  # 악세사리 종류별로 리스트를 저장하는 사전

for _ in range(tc):
    n = int(input())  # 각 테스트 케이스에 대한 입력 수
    for _ in range(n):
        # 아이템과 종류를 입력 받음 (예: "목걸이 gold"와 같은 형태)
        item, category = input().strip().split()
        
        # 종류를 키로, 아이템을 값으로 사전에 추가
        accessory_dict[category].append(item)

# 결과 출력
for category, items in accessory_dict.items():
    print(f"{category}: {', '.join(items)}")
'''