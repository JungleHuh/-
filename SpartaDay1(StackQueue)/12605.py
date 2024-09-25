for i in range(int(input())):
    n = input().rstrip().split()
    print(f"Case #{i+1}: {' '.join(n[::-1])}")  # 중첩된 따옴표 문제 해결
