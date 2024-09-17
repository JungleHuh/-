coins = list(map(int, input().split()))
coins.sort()

result = 0
k = 1

for coin in coins:
    if k > coin:
        break
    else:
        k += coin
print(k)
    
