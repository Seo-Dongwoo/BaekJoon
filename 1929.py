M, N = map(int, input().split())
sosu = []

for i in range(M, N+1):
    if i == 0:
        continue
    elif i == 2:
        sosu.append(i)
    for j in range(2, i):
        if i%j == 0:
            break
        elif i-1 == j:
            sosu.append(i)

for i in sosu:
    print(i)
