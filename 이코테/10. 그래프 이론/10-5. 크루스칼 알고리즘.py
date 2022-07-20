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


v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

for i in range(1, v + 1):  # 부모테이블에서 자기자신을 부모로 초기화
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):  # 사이클이 발생하지 않는 경우에만 집합에 포함
        union_parent(parent, a, b)
        result += cost

print(cost)

# 입력갑
"""
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 23
6 7 25
"""

# 출력값
"""
159
"""

