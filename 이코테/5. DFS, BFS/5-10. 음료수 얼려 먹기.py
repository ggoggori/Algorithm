"""
해설은 dfs로 풀었다.
나는 bfs로 풀었는데, 코드가 너무 길고 깔끔하지 못한 것 같다.
"""
from collections import deque

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(array, start):
    queue = deque([start])
    array[start[0]][start[1]] = 1
    while queue:
        v = queue.popleft()
        x, y = v[0], v[1]
        target = [
            (x + i, y + j)
            for i, j in zip(dx, dy)
            if 0 <= x + i < len(array) and 0 <= y + j < len(array[0])
        ]
        # 상하좌우로 가능한 좌표 찾기.
        for i, j in target:
            if not array[i][j]:
                array[i][j] = 1  # 방문처리
                queue.append((i, j))
    return array


count = 0
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            array = bfs(array, (i, j))
            count += 1

print(count)
