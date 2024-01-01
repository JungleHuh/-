data = input()
count0 = 0
count1 = 0 

if data[0] == '1':
    count0 += 1
else:
    count1 += 1
# data[i] != data[i+1] -> 연속된 수라면, 상황을 고려하지 않고 넘어감.
# 내가 이해하지 못했던 포인트
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
print(min(count0, count1))
