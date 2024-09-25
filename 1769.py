import sys
input = sys.stdin.readline

n = input().strip()
total_sum = 0
count = 0
while len(n) > 1:
    total_sum = 0  # 각 루프에서 초기화
    for i in n:
        total_sum += int(i)
    count +=1
    n = str(total_sum)  # 다시 문자열로 변환

print(count)

if len(n) == 1:
    if int(n) % 3 == 0:
        print('YES')
    elif total_sum == 3 or total_sum == 6 or total_sum == 9:
        print('YES')
    else:
        print('NO')