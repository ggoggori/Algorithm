n = int(input())
dp = [0] * (n+1) # dp tabel 초기화

for i in range(2,n+1): # 헷갈렸던게, 1에서 계산횟수가 1번인 줄 알았음. 이미 1이기 때문에 횟수 0번으로 1을 만들 수 있음. 그래서 2부터 시작.
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    elif i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)