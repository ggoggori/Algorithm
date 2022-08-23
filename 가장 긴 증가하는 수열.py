n = 7
array = [15,11,4,8,5,2,4]
array.reverse()
dp = [1 for i in range(n)]
for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)