n = int(input())
dp = [0] * n

dp[0] = 1
dp[1] = 3
for i in range(2,n): 
    dp[i] = (dp[i-1] + 2*dp[i-2]) % 796796
    # 점화식을 세우면 쉽게 풀 수 있다.
    # dp 문제라고 생각이 들면 점화식을 먼저 세워보자!!
print(dp[n-1])