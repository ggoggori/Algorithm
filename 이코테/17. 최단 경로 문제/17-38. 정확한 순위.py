# 푼 횟수 : v
# a에서 b로 이동이 가능하거나 b에서 a로 이동이 가능하면 순위 비교가 가능해짐.
n, m = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

# n행과 n열에서 1(서로 이어져있음을 의미)인 것을 세고 만약 n-1과 같다면 순위 비교가 가능한 것으로 판단
# n-1인 이유는 자기 자신은 0이기 때문
count = 0
for k in range(1,n+1):
    sums = sum(graph[k])
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j == k: 
                sums += graph[i][j]
    if sums == n-1:
        count += 1
            
print(count)