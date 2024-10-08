import sys
input = sys.stdin.readline

std = input().rstrip()  # 기준 문자열
find = input().rstrip()  # 찾을 문자열

cnt = 0  # 찾은 횟수
idx = 0  # 탐색 인덱스

# 기준 문자열의 남은 부분이 찾을 문자열보다 짧으면 종료
while idx + len(find) <= len(std):
    # 현재 부분 문자열이 찾을 문자열과 동일한지 비교
    if std[idx:idx + len(find)] == find:
        cnt += 1  # 찾은 횟수 증가
        idx += len(find)  # 찾은 문자열 길이만큼 인덱스 이동
    else:
        idx += 1  # 일치하지 않으면 인덱스를 1씩 이동

print(cnt)
