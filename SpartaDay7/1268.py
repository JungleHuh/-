n = int(input())  # 학생 수
classes = [list(map(int, input().split())) for _ in range(n)]  # 각 학생의 1학년부터 5학년까지 반 정보

# 각 학생이 몇 번 같은 반이었는지 계산할 리스트
same_class_count = [0] * n

# 각 학생마다 다른 학생들과 몇 번 같은 반이었는지 비교
for i in range(n):  # i번 학생
    for j in range(n):  # j번 학생
        if i != j:  # 자기 자신과 비교는 할 필요 없음
            for k in range(5):  # 1학년부터 5학년까지
                if classes[i][k] == classes[j][k]:  # 같은 반이었던 경우
                    same_class_count[i] += 1
                    break  # 한 번이라도 같은 반이면 더 이상 그 학년에 대해 비교할 필요 없음

# 같은 반이 가장 많은 학생을 찾음
max_count = max(same_class_count)
leader = same_class_count.index(max_count) + 1  # 학생 번호는 1부터 시작하므로 +1

print(leader)
