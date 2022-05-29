import sys

input = sys.stdin.readline

N = int(input())
input_array = list(map(int, input().split()))
dp = [x for x in input_array]

for i in range(N):
    for j in range(i):
        if input_array[i] > input_array[j]:
            dp[i] = max(dp[i], dp[j] + input_array[i])

print(max(dp))