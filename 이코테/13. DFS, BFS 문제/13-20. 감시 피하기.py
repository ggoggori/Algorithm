# 푼 횟수: v

from itertools import combinations
import copy

n = int(input())
graph = []
for i in range(n):
    graph.append(input().split())

coor = [(i, j) for i in range(n) for j in range(n) if graph[i][j] != "S" and graph[i][j] != "T"]
# n이 3부터 6까지이기 때문에 가능한 모든 조합을 구하는 게 가능하다고 판단
coor_ = list(combinations(coor, 3))

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


def check_student(i, j, graph):
    num = 0
    for di in range(4):
        next_i, next_j = i, j
        while True:
            next_i, next_j = next_i + dx[di], next_j + dy[di]
            if 0 <= next_i and next_i < n and 0 <= next_j and next_j < n:
                if (
                    graph[next_i][next_j] == "T" or graph[next_i][next_j] == "O"
                ):  # 계속해서 같은 방향을 보면서 학생이 아닌게 나오면 break
                    break
                elif (
                    graph[next_i][next_j] == "S"
                ):  # 학생이 나오면 1을 더해줌! (다른 방향에서도 나올 수 있기 때문에 아예 return하지는 않는다!)
                    num += 1
                    break
            else:
                break
    return num


flag = False
for co in coor_:
    answer = 0
    copy_graph = copy.deepcopy(graph)
    for x, y in co:
        copy_graph[x][y] = "O"

    for i in range(n):
        for j in range(n):
            if copy_graph[i][j] == "T":  # 선생님 좌표를 만나면
                answer += check_student(i, j, copy_graph)  # 선생님 좌표에서 학생을 볼 수 있는지 판단
    if answer == 0:
        flag = True
        break

if flag == True:
    print("YES")
else:
    print("NO")

