x = int(input())

dp = [0] * (x + 1)
dp[0] = 0
for n in range(1, x + 1):
    dp[n] = dp[n-1] + 1
    dp[n] = min(dp[n], dp[n // 2], dp[n // 3], dp[n // 5])
