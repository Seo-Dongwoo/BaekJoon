import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
result = [1]*N

for i in range(1,N):
    for j in range(i):
        if A[j] < A[i]:
            result[i] = max(result[i], result[j]+1)

print(max(result))