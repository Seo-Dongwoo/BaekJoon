import sys
N, M = map(int, sys.stdin.readline().split())

def fiveCount(N):
    count = 0
    while N != 0:
        N = N // 5
        count += N
    return count

def twoCount(N):
    count = 0
    while N != 0:
        N = N // 2
        count += N
    return count

if M == 0:
    print(0)
else:
    print(min(twoCount(N) - twoCount(M) - twoCount(N - M), fiveCount(N) - fiveCount(M) - fiveCount(N - M)))