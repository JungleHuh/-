import sys
input = sys.stdin.readline

n = int(input())  
lst = []
for _ in range(n):
    lst.append(list(input().strip()))  # 리스트에 문자열을 리스트로 저장

for i in lst:
    if i == i[::-1]:
        print(0)  
    else:
        found = False
        for j in range(len(i)):
            temp = i[:j] + i[j+1:]  # j번째 문자를 제거한 리스트 생성
            if temp == temp[::-1]:  # j번째 문자를 제거하고 회문인지 확인
                print(1)  # 한 문자를 제거해서 회문이 되면 1 출력
                found = True
                break
        if not found:
            print(2)  # 한 문자를 제거해도 회문이 안 되면 2 출력
