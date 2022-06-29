n, m = 4, 7
INF = int(1e9)
graph = [[], [INF, 0, 4, INF, 6], [INF, 3, 0, 7, INF], [INF, 5, INF, 0, 4], [INF, INF, INF, 2, 0]]

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("infinity")
        else:
            print(graph[a][b], end=" ")
    print()
