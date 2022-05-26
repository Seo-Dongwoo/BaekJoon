import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
reverse_case = A[::-1]

increase = [1 for i in range(N)]
decrease = [1 for i in range(N)]
result = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            increase[i] = max(increase[i], increase[j] + 1)
        if reverse_case[j] < reverse_case[i]:
            decrease[i] = max(decrease[i], decrease[j] + 1)

for i in range(N):
    result[i] = increase[i] + decrease[N - i - 1] -1

print(max(result))