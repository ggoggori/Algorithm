# 문제 이해를 똑바로 할 것!!!

n, m = list(map(int, input().split()))

array = []
for i in range(n):
    row = list(map(int, input().split()))
    array.append(row)

houses = []
chickens = []
answer = []

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            houses.append((i, j))
        elif array[i][j] == 2:
            chickens.append((i, j))

for house in houses:
    distance = n * n
    for chicken in chickens:
        temp = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
        if distance > temp:
            distance = temp
    answer.append(distance)

answer.sort()
print(sum(answer[:m]))

