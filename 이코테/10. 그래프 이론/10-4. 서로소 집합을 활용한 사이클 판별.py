# 부모 노드를 찾는 함수.
# 인자 parent는 부모 테이블을 뜻함.
# 10-1.py와는 다르게 바로 부모테이블을 갱신하여 갱신속도를 크게 줄일 수 있다.(경로압축방법)
from gettext import find


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
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i

cycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

# 입력값
"""
3 3
1 2
1 3
2 3
"""
# 출력값
"""
사이클이 발생했습니다.
"""

