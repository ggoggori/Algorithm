from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(graph, start):
    i, j = start[0], start[1]
    queue = deque([(i, j)])  # 첫번째 방문지점을 queue에 삽입

    while queue:
        v = queue.popleft()  # bfs
        target = [
            (v[0] + i, v[1] + j) for i, j in zip(dx, dy) if 0 <= v[0] + i < n and 0 <= v[1] + j < m
        ]  # n,m 범위 내에 있는 좌표중 현재 탐색지점에서 상,하,좌,우를 살핌.
        for i, j in target:
            if graph[i][j] == 1:  # 가능한 상하좌우 좌표 중, 해당 좌표가 처음 방문하는 좌표라면,
                queue.append((i, j))
                graph[i][j] = (
                    graph[v[0]][v[1]] + 1
                )  # 이전 거리 + 1을 함. 이렇게 되면 (n-1,m-1) 좌표에는 최단거리가 기록됨.
    return graph[n - 1][m - 1]
