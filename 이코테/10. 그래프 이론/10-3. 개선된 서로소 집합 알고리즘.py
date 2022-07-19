# 부모 노드를 찾는 함수.
# 인자 parent는 부모 테이블을 뜻함.
# 10-1.py와는 다르게 바로 부모테이블을 갱신하여 갱신속도를 크게 줄일 수 있다.(경로압축방법)
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

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

print("부모 테이블: ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")

# 입력값 예시
"""
6 4
1 4
2 3
2 4
5 6
"""

# 출력값 예시
"""
각 원소가 속한 집합: 1 1 1 1 5 5 
부모 테이블: 1 1 1 1 5 5 
"""

