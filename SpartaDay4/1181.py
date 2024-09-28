
n = int(input())
word = []

for i in range(n):
    word.append(input())

# Sort 하면 a,b,c,d 순서대로 됨. 그러니까 각 길이별로 Sort 해주고 Merge -> Merge Sort
word = set(word)
word.sort()
word.sort(key = len)

for i in word:
    print(i)


               