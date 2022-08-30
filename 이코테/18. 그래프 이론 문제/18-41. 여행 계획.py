# 푼 횟수 : v 
n, m = map(int,input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

graph = [[] for i in range(n+1)]    

for i in range(1, n+1):
    temp = map(int,input().split())

    for idx, j in enumerate(temp, 1):
        if j == 1:
            graph[i].append(idx) # 연결 정보가 들어있는 graph 만들어줌

route = list(map(int,input().split()))

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

for idx, i in enumerate(graph): # 이부분을 답처럼 입력받을 때 그냥하면 코드가 간결해질텐데!!!
    for j in i:
        union_parent(parent, idx, j)

result = []
for i in route:
    result.append(find_parent(parent, i))

if all(result) == True:
    print('YES')
else:
    print('NO')