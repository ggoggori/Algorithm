n, m = 2, 15
array = [2, 3]

dp = [10001] * (m + 1)
dp[0] = 0
for i in array:
    for j in range(i, m + 1):
        dp[j] = min(dp[j - i] + 1, dp[j])

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])
