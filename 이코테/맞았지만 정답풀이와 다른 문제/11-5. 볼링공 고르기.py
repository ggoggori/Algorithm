# 푼 횟수 : v
from itertools import combinations

n, m = 8, 5
inputs = [1, 5, 4, 3, 2, 4, 5, 2]

len([i for i in list(combinations(inputs, 2)) if i[0] != i[1]])

