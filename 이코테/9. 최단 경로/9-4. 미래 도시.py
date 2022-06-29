n, m = 5, 7
given = [(1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (3, 5), (4, 5)]
x, k = 4, 5
INF = int(1e9)

given.extend([(i[1], i[0]) for i in given])
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            graph[i][j] = 0

for coor in given:
    graph[coor[0]][coor[1]] = 1

for k in range(n + 1):  # graph가 1부터 이기때문에 모든 range에 1부터 시작을 넣어주면 좋음! 하지만 나는 바보라서 그것까지는 생각못했다,,!
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance > INF:
    print("-1")
else:
    print(distance)
