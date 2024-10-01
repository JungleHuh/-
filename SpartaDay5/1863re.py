import sys
input = sys.stdin.readline

def main():
    n = int(input()) 
    building = [0]
    ans = 0

    for _ in range(n):
        x, current_h = map(int, input().split())
        
        if current_h > building[-1]:
            ans += 1
            building.append(current_h)
        else:
            while building[-1] > current_h:
                building.pop()

            if building[-1] <current_h:
                ans +=1
                building.append(current_h)
    print(ans)

if __name__ == '__main__':
    main()

