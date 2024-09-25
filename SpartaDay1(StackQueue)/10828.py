import sys
input = sys.stdin.readline

n = int(input())  # 명령의 개수를 입력받음
stack = []

for _ in range(n):
    k = input().strip().split()  # 입력된 문자열을 공백 기준으로 분리
    command = k[0]  # 첫 번째 요소는 명령어
    if command == 'push':
        value = int(k[1])  # 두 번째 요소는 값
        stack.append(value)  # 스택에 값 추가
    elif command == 'pop':
        if stack:  # 스택이 비어있지 않을 경우
            m = stack.pop()
            print(m)
        else:
            print(-1)  # 스택에서 값 제거
    elif command == 'top':
        if stack:  # 스택이 비어있지 않을 경우
            print(stack[-1])  # 가장 상단의 값 출력
        else:
            print(-1)  # 스택이 비어있을 경우
    elif command == 'size':
        print(len(stack))  # 스택의 크기 출력
    elif command == 'empty':
        print(1 if not stack else 0)  # 스택이 비어있으면 1, 아니면 0
  

