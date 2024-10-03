import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))

lst.sort()

print(round(sum(lst)/n))
print(lst[n//2])
cnt = Counter(lst)
limit = cnt.most_common()
if len(limit) > 1 and limit[0][1] == limit[1][1]:
    print(limit[1][0])
else:
    print(limit[0][0])
print(lst[-1] - lst[0])