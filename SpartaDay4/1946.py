import sys
input = sys.stdin.readline

tc = int(input())
results = []

for _ in range(tc):
    n = int(input())
    versus_table = []

    for _ in range(n):
        # map을 사용하여 입력 처리
        test, interview = map(int, input().split())
        versus_table.append((test, interview))

    # 선발할 수 있는 지원자의 수를 저장
    selected_count = 0

    for i in range(n):
        is_selected = True  # 현재 지원자가 선발될 수 있는지 여부

        for j in range(n):
            if (versus_table[i][0] > versus_table[j][0] and
                versus_table[i][1] > versus_table[j][1]):
                is_selected = False  # 두 성적 모두 떨어지면 선발 불가
                break
        
        if is_selected:
            selected_count += 1  # 선발 가능하면 카운트 증가

    results.append(selected_count)

# 결과 출력
for result in results:
    print(result)
