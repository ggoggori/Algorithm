# 푼 횟수 : v
# 정답 풀이가 훨씬 깔끔한 것 같다!!! 다음에 풀 때는 정답 풀이 스타일로 풀어보기!

n, k = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

dx = [-1,1,0,0] #상하좌우
dy = [0,0,-1,1]

visited = [[0]*(n)  for _ in range(n)] # 방문했던 순간의 초를 기록하는 테이블

for sec in range(1, s+1):
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0 and visited[i][j] < sec: # 만약 바이러스면서, 테이블 갱신이 아직 안된 상태라면
                for t in range(4):
                    x_ = i+dx[t]
                    y_ = j+dy[t]
                    if x_ >= 0 and x_ < n and y_ >= 0 and y_ < n:
                        if graph[x_][y_] == 0: # 아직 바이러스가 들어갈 공간이 있다면
                            graph[x_][y_] = graph[i][j] # 바이러스 주입
                            visited[x_][y_] = sec # 테이블에 초 갱신
                        elif graph[i][j] < graph[x_][y_] and visited[x_][y_] == sec:
                            # 만약 다른 바이러스가 들어가 있더라도 이번에 갱신된 바이러스면서, 현재 바이러스보다 크면 작은 바이러스로 다시 갱신해줌
                            graph[x_][y_] = graph[i][j]
    
    flag = False # 아래는 이미 바이러스 전파가 다 끝났다면 break 걸어주기 위해서 삽입! 없으면 에러 
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                flag = True
    if flag == False:
        break

print(graph[x-1][y-1])