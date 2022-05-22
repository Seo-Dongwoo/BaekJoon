import sys
A, B = map(int, sys.stdin.readline().split())
arr = []

for i in range(1, min(A,B)+1):
    if A % i == 0 and B % i == 0:
        arr.append(i)

print(max(arr))
print(max(arr) * (A // max(arr)) * (B//max(arr)))
