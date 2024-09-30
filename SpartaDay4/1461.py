n, m = map(int,input().split())

book = list(map(int,input().split()))
pos = []
neg = []
l = []
for i in book:
	if i > 0:
		pos.append(i)
	else:
		neg.append(abs(i))
pos.sort(reverse=True)
neg.sort(reverse=True)

for i in range(len(pos)):
	if i % m == 0:
		l.append(pos[i])
for i in range(len(neg)):
	if i % m == 0:
		l.append(neg[i])

l.sort()
ans = 2* sum(l) - l[-1]
print(ans)