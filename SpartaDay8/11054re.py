def solve(n, lst):
    dp_increase = [0] * n
    for i in range(1,n):
        for j in range(i):
            if lst[i] > lst[j]:
                dp_increase[i] = max(dp_increase[i], dp_increase[j]+1)
    
    dp_decrease = [0]* n

    lst_reverse = lst[::-1]
    for i in range(1,n):
        for j in range(i):
            if lst_reverse[i] > lst_reverse[j]:
                dp_decrease[i] = max(dp_decrease[i], dp_decrease[j]+1)

    ans = 0
    for i in range(n):
        ans = max(ans, dp_increase[i] + dp_decrease[::-1][i])
    return ans +1

n = int(input())
lst = list(map(int, input().split()))
print(solve(n,lst))