from collections import Counter
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

count = Counter(A)
stack=[]
answer = [-1] * N
stack.append(0)

for i in range(N):
    while stack and count[A[stack[-1]]] < count[A[i]]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)
