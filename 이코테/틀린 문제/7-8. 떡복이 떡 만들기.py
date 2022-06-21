n, m = 4, 6
array = [19,15,10,17]

for i in range(max(array),0,-1):
    if m == sum([0 if j<=i else j-i for j in array]):
        print(i)
# 문제에서 1억까지 높이가 주어진다고 했기 때문에 순차탐색과 같이 이딴 식으로 풀면 시간초과임.