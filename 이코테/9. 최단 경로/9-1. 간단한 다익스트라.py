INF = int(1e9)
n,m = 6,11
start = 1
graph = [[],[(2,2),(3,5),(4,1)],[(3,3),(4,2)],[(2,3),(6,5)],[(3,3),(5,1)],[(3,1),(6,2)],[]]
visited = [False] * (n+1)
distance = [INF] * (n+1)

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1): # 모든 노드를 순회하면서, "방문하지 않았고" / "start로 부터 가장 가까운 거리를 갖는" 노드의 index를 반환함.
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]: #시작 노드와 연결된 노드들간의 최소 거리를 기록.
        distance[j[0]] = j[1]
    
    for _ in range(n-1): # 시작 노드를 제외한 노드의 갯수만큼 반복.
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1] # 현재 검사 중인 노드와 start 간의 최단 거리에 검사중인 노드와 연결된 거리를 더함.
            if cost < distance[j[0]]: # 만약 cost(다른 곳을 거쳐서 가는 거리)가 현재의 최단거리보다 작다면
                distance[j[0]] = cost # 최단거리를 cost로 교체함.

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])