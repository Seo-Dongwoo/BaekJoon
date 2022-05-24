N = int(input())
card = [0]
card += list(map(int, input().split())) # 카드 갯수 마다의 카드팩 가격

dp = [0] * (N+1)
dp[1] = card[1]
dp[2] = min(card[2], card[1]*2)

for i in range(3, N+1):
    dp[i] = card[i] #자기 자신으로 만드는 경우
    for j in range(1, i//2 + 1):
        dp[i] = min(dp[i], dp[j] + dp[i-j])
print(dp[N])