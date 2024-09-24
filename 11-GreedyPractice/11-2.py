import sys
input = sys.stdin.readline

data = input().strip()  # 개행문자 제거
start = int(data[0])  # 첫 번째 문자를 정수로 변환

result = start  # result를 첫 번째 숫자로 초기화

for i in range(1, len(data)):
    num = int(data[i])  # 각 문자를 정수로 변환
    if result <= 1 or num <= 1:  # 현재 결과가 0이거나 num이 0이면 더하기
        result += num
    else:
        result *= num  # 그렇지 않으면 곱하기

print(result)
