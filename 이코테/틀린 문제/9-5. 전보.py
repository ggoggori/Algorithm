"""
거의 다 맞았는데, 다시 풀어보기!

"""
import heapq

n, m, c = 3, 2, 1
given = [(1, 2, 4), (1, 3, 2)]
INF = int(1e9)

graph = [[] for _ in range(n + 1)]

for coor in given:
    graph[coor[0]].append(coor[1:])

distance = [INF for _ in range(n + 1)]


def dikjstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        print(now)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)

