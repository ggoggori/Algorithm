'''
 푸는데 오래걸림...
 방식은 금방생각 해냈는데, if문 활용에서 문제를 제대로 반영하지 못해서,,, 그 부분을 해결하느라 오래걸렸다.
'''
n = int(input())
graph = []
for _ in range(n):
    graph.append([i for i in input()])

answer = 0

def check_max(graph): # 주어진 그래프에서 가장 많이 연결된 색을 찾는 함수
    global answer
    rows = [graph[i] for i in range(n)] # row list
    cols = [[graph[i][j] for i in range(n)] for j in range(n)] # col list
    check_list = rows + cols

    for i in check_list:
        prev = None 
        count = 1
        for t in i:
            if t == prev: #현재가 이전과 같으면 count에 +1
                count+=1
            else:
                count = 1   
            answer = max(answer, count) # answer와 count 비교
            prev = t

for i in range(n):
    for j in range(n): 
        if i+1 < n and graph[i][j] != graph[i+1][j]: # 각 좌표를 돌면서 아래와 오른쪽만 확인, 왼쪽과 위는 볼 필요가 없음. 좌표가 바뀌면서 계속 확인할 수 있기 떄문에
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j] # swap
            check_max(graph) # check
            graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j] # 원위치
        
        if j+1 < n and graph[i][j+1] != graph[i][j]:
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            check_max(graph)
            graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]

print(answer)