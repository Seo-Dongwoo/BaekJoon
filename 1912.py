import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

for i in range(1,N):
    A[i] = max(A[i], A[i-1] + A[i])

print(max(A))