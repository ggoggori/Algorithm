# 푼 횟수 : v


"""
내가 푼 풀이
주어진 동전으로 가능한 모든 조합을 구하고, 
1부터 모든 조합 중 가장 큰 수까지의 set을 만든다.
그리고 차집합을 구해서 거기서 가장 작은 수를 정답으로 출력한다.
"""
# from itertools import combinations

# n = 5
# array = [3, 2, 1, 1, 9]

# result = set()

# for i in range(1, n + 1):
#     for items in list(combinations(array, i)):
#         result.add(sum(items))

# answer = set([i for i in range(1, max(result) + 1)])
# min(answer - result)
