from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)  # 모든 노드에 대한 진입차수는 0으로 초기화

graph = [[] for i in range(v + 1)]  # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []  # 알고리즘 수행결과를 담을 리스트
    q = deque()

    for i in range(1, v + 1):  # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i)

    while q:  # 큐가 빌 때까지
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1  # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
            if indegree[i] == 0:
                q.append(i)

    for i in result:  # 결과 출력
        print(i, end="")


topology_sort()

# 입력값
"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""

# 출력값
"""
1 2 5 3 6 4 7
"""
