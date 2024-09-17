'''
import sys
input = sys.stdin.readline

n = int(input())
k = len(str(n)) //2
lista = []
listb = []

for i in range(k):
    lista.append(str(n)[i])
for j in range(k,len(str(n))):
    listb.append(str(n)[j])

a = sum(lista) 
b = sum(listb)
if a == b:
    print("LUCKY")
else:
    print("READY")
'''

#문제점 (1): 정수 - 문자열 교환할 떄 깔끔하게 정리하지 않아서, sum에서 문자열을 정수처럼 더하려고 했다.
#문제점 (2): iterable만 append할 수 있음.

import sys
input = sys.stdin.readline

n = int(input().strip())  # 입력값에서 공백 및 줄 바꿈 문자 제거

# 입력된 숫자를 문자열로 변환하여 리스트에 넣기
num_str = str(n)
k = len(num_str) // 2
lista = list(map(int, num_str[:k]))
listb = list(map(int, num_str[k:]))

# 리스트 합계 계산
sum_a = sum(lista)
sum_b = sum(listb)

if sum_a == sum_b:
    print("LUCKY")
else:
    print("READY")