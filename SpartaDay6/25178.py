import sys
input = sys.stdin.readline

n = int(input())
str_1 = input().strip()
str_2 = input().strip()

# 리스트에 모음(a, e, i, o, u)을 제외한 문자만 남기기
lst_1 = [char for char in str_1]
lst_2 = [char for char in str_2]

# 첫 문자와 마지막 문자가 같은지 확인
if str_1[0] == str_2[0] and str_1[-1] == str_2[-1]:
    lst_1.sort()
    lst_2.sort()
    if lst_1 == lst_2:
        lst_1 = [char for char in str_1 if char not in 'aeiou']
        lst_2 = [char for char in str_2 if char not in 'aeiou']
        if lst_1 == lst_2:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
else:
    print('NO')

