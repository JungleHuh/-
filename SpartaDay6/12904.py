def can_convert(S, T):
    # T가 S로 변환 가능한지 확인
    while len(T) > len(S):
        if T[-1] == 'A':
            T = T[:-1]  # T에서 A를 제거
        elif T[-1] == 'B':
            T = T[:-1][::-1]  # T에서 B를 제거하고 뒤집기
        else:
            break  # T의 마지막이 'A'나 'B'가 아닐 경우 종료

    # 최종적으로 T와 S가 같아야 변환 가능
    return T == S

# 사용자 입력 받기
S = input().strip()
T = input().strip()

# 변환 가능 여부 판단
if can_convert(S, T):
    print(1)
else:
    print(0)
