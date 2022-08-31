# 푼 횟수 : v
# graph를 오름차순으로 정렬하고 union을 진행해야되는 걸 잊지말자!!
# 최소비용을 찾는 것이기 때문에 가장 적은 비용을 가지는 edge부터 추가해야 함!

n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph.sort()
total_cost = sum([i[0] for i in graph])

parent = [i for i in range(n)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
for cost, a, b in graph:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total_cost - result)