import sys
input = sys.stdin.readline

# 입력받은 숫자 문자열을 리스트로 변환
n = [char for char in input().strip()]
n.sort(reverse=True)

# 0이 없다면 3의 배수를 만들 수 없음
if '0' not in n:
    print(-1)
else:
    # 자리 수의 합이 3의 배수이면 3의 배수로 만들 수 있음
    if sum(map(int, n)) % 3 == 0:
        print(''.join(n)) 
    else:
        print(-1)

# sort는 내림차순 계속 이어진다.