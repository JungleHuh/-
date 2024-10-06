import sys
input = sys.stdin.readline

n = int(input())
square = 1
ans = 10
while n >= square*2:
    square = square*2
    ans +=1
print(ans)


# daldidalgo + daldidan
# d +a + l + d + i + d + a + l + g + o + daldid + n -> 12번
# d + a + l + d + i + ( dal) + g + o + (daldida) + n -> 10번
# d + a + l + d  + i + d + a + l
# 여기서 주안점 둬야하는 것은 dal(3입력 후 재사용) or daldi(5 입력 후 재사용) or daldida(7입력후 재사용)

# daldidalgo + daldidalgo + daldidan
# 2번 넘어가면서부터는 daldidalgo 그냥 반복할 수 있음
# 2번쨰부터는 이게 최소임 d+a + l +d + i + dal +g +o + daldidalgo + daldida + n 

# daldidalgo + daldidalgo + daldidalgo + daldidan
# d + a + l + d + i + (dal) + g + o + (daldidalgo) + (daldidalgodaldida) + n

# daldidalgo + daldidalgo + daldidalgo + daldidalgo + daldidan
# d + a + l + d + i + (dal) + g + o + (daldidalgo) + (daldidaldodaldidalgodaldida) + n 12