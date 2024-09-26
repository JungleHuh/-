n = int(input())
password = []

for i in range(n):
    password.append(input())

for i in range(n):
    for j in range(i,n):
        if password[i][::-1] == password[j]:
            print(len(password[i]), password[i][len(password[i])//2])
            exit()
