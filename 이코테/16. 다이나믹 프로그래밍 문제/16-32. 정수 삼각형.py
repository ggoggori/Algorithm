# 푼 횟수 : v
# 점화식 : dp[i][j] = graph[i][j] + max(dp[i-1][j], dp[i-1][j-1])

n = int(input())
graph = []
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

dp = []  # dp 테이블을 따로 만들었는데, 그냥 grpah 리스트를 바로 dp 테이블로 활용해도 됨 ㅠㅠ
for i in graph:
    temp = []
    for j in range(len(i)):
        temp.append(0)
    dp.append(temp)

dp[0][0] = graph[0][0]

for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = graph[i][j] + dp[i - 1][j]
        elif j == (len(dp[i]) - 1):
            dp[i][j] = graph[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = graph[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])

print(max(dp[n - 1]))

