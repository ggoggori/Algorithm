# 푼 횟수 : v
# 풀이보고 혼자서 다시 풀어봄!
# 풀이는 가능한 조합을 구할 때도 dfs를 사용했는데, 나는 조합을 사용해서 풀었다!

from itertools import combinations
from collections import deque
import copy

n, m = list(map(int, input().split()))
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


def virus(x, y):
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = dx[i], dy[i]
            next_x = x + next_x
            next_y = y + next_y

            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
                if temp[next_x][next_y] == 0:
                    temp[next_x][next_y] = 2
                    queue.append((next_x, next_y))


xy = [(i, j) for j in range(m) for i in range(n) if graph[i][j] == 0]  # 벽이 될 수 있는 좌표들
xys = list(combinations(xy, 3))  # 가능한 모든 벽들의 조합

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

answer = 0
for xy in xys:
    count = 0
    temp = copy.deepcopy(graph)

    for x, y in xy:
        temp[x][y] = 1

    for i in range(n):  # 바이러스 퍼트리기
        for j in range(m):
            if temp[i][j] == 2:
                virus(i, j)

    for i in range(n):  # 바이러스가 퍼진 뒤 안전지대의 크기 구하기
        for j in range(m):
            if temp[i][j] == 0:
                count += 1

    if answer < count:  # 이번 안전지대가 더 크다면 정답 교체
        answer = count

print(answer)
