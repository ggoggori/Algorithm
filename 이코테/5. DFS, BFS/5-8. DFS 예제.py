def dfs(graph, i, visited):
    visited[i] = True
    print(i, end="")
    for i in graph[i]:
        if visited[i] == False:
            dfs(graph, i, visited)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
visited = [False for i in range(len(graph))]

dfs(graph, 1, visited)

# 1부터 시작하기 때문에 index를 맞춰주기 위해서 graph의 첫번째 리스트가 비어있다는 것을 명심하기!!
