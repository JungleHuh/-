# 두 개의 문자열 입력받기
l = [input() for _ in range(2)]
l.sort(key=len)  # 길이 기준으로 정렬
w1, w2 = l
l1, l2 = len(w1), len(w2)

# dp 배열 초기화 (l1+1) x (l2+1) 크기
dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

# LCS 계산
for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if w1[i - 1] == w2[j - 1]:  # w1[i-1]와 w2[j-1] 비교
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# LCS의 길이 출력
print(dp[l1][l2])  # 가장 긴 공통 부분 수열의 길이

# LCS의 값 출력
lcs_length = dp[l1][l2]  # LCS의 길이
lcs = []  # LCS 저장을 위한 리스트

# LCS 문자열 생성
i, j = l1, l2
while i > 0 and j > 0:
    if w1[i - 1] == w2[j - 1]:  # 같은 문자를 찾으면
        lcs.append(w1[i - 1])  # LCS에 추가
        i -= 1
        j -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:  # 위쪽에서 더 긴 경우
        i -= 1
    else:  # 왼쪽에서 더 긴 경우
        j -= 1

# LCS 문자열 출력 (거꾸로 저장되어 있으므로)
lcs.reverse()
print(''.join(lcs))  # 가장 긴 공통 부분 수열
