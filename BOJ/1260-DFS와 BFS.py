from collections import deque

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

graph = [sorted(i) for i in graph]

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end= ' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

visited = [False for _ in range(len(graph))]
dfs(graph, start, visited)

print()

visited = [False for _ in range(len(graph))]
bfs(graph, start, visited)