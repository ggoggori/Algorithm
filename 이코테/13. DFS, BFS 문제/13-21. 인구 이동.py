# 푼 횟수: v
# 책이랑 거의 동일한 방식으로 풀었따!!

from collections import deque

n, l, r = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, i, j, visited):
    result = [(i, j)]
    queue = deque([(i, j)])
    visited[i][j] = True  # 방문처리

    while queue:
        now = queue.popleft()  # 꺼내기
        for c in range(4):
            x, y = now[0] + dx[c], now[1] + dy[c]
            if (
                0 <= x and x < n and 0 <= y and y < n and visited[x][y] == False
            ):  # 다음에 방문할 곳이 방문안한 곳이라면
                if l <= abs(graph[x][y] - graph[now[0]][now[1]]) <= r:  # 또한 기준에 부합한다면
                    visited[x][y] = True  # 방문처리하고
                    queue.append((x, y))  # 큐에 삽입
                    result.append((x, y))  # 같은 연합처리

    return result, visited  # result에는 같은 연합인 도시들의 좌표가 있음


count = 0
while True:
    results = []
    visited = [[False] * (n) for i in range(n)]  # 방문 초기화

    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:  # 방문을 아직안했다면
                result, visited = bfs(graph, i, j, visited)  # bfs
                if len(result) > 1:
                    # 특정 좌표가 연합이 없이 혼자라면 해당 좌표만을 반환하기 때문에 적어도 2개이상의 좌표, 즉 연합이 완성되었을 때만 결과에 삽입!
                    results.append(result)

    if len(results) == 0:
        break

    for result in results:
        temp = int(sum([graph[x][y] for x, y in result]) / len(result))  # 인구이동 값
        for x, y in result:
            graph[x][y] = temp

    count += 1

print(count)
