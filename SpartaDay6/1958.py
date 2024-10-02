'''
a = [ char for char in input()]
b = [ char for char in input()]
c = [ char for char in input()]

# LCS 문제...!, 일단은 혼자 접근해보고 안되면, 이코테 책보면서 다시 풀어보자
# 

# 일단 크기 줄이기 위해서 최대로 작은 문자열을 기준으로 삼는다.
min_str = min(len(a), len(b), len(c))

'''

l = [input() for _ in range(3)]
l.sort(key = len)
word_1, word_2, word_3 = l
l1,l2,l3 = len(word_1), len(word_2), len(word_3)

dp = [[[0]* (l1+1) for _ in range(l2+1)] for _ in range(l3+1)]
print(dp)
for k in range(1, l3+1):
    for j in range(1, l2+1):
        for i in range(1, l1+1):
            if word_1[i-1] == word_2[j-1] == word_3[k-1]:
                dp[k][j][i] = dp[k-1][j-1][i-1]+ 1
            else:
                dp[k][j][i] = max(dp[k-1][j][i], dp[k][j-1][i], dp[k][j][i-1])
print(dp[-1][-1][-1])