# 푼 횟수 : v
import heapq

n, m = 6, 7
inputs = """3 6
4 3
3 2
1 3
1 2
2 4
5 2"""

graph = [[] for i in range(n+1)]
for i in inputs.split('\n'):
    a,b = list(map(int, i.split()))
    graph[a].append(b)
    graph[b].append(a) # 양방향 통로이기 때문에

INF = 1e9
distance = [INF for i in range(n+1)] # dp 테이블

start = 1
q = []
heapq.heappush(q, (0, start)) #cost,start
distance[start] = 0

while q: # 다익스트라
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

distance = [-1 if i == INF else i for i in distance]
answer = max(distance)
for idx, i in enumerate(distance):
    if i == answer:
        print(idx,i, sum([True for j in distance if j==answer]))
        break
