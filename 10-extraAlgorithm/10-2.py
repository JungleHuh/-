# 약수가 존재한다면, 어차피 대칭이니 제곱근으로 알고리즘 탐색 범위 줄여서 효율성 높임

import math

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

print(is_prime(4))
print(is_prime(7))