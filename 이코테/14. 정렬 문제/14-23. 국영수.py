# 푼 횟수 : v
n = int(input())
graph = []
for _ in range(n):
    temp = input().split()
    temp[1:] = list(map(int, temp[1:]))
    graph.append(temp)

for i in sorted(graph, key=lambda x: (-x[1], x[2], -x[3], x[0])):
    print(i[0])
