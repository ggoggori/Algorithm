from itertools import permutations

coor = input()

i = int(coor[1])
j = ord(coor[0]) - 96

temp = list(permutations([1, 2, -2, -1], 2))
temp = [
    i for i in temp if i[0] + i[1] != 0
]  # package를 사용해서 경우의 수를 구했는데, 경우의 수가 많지 않다면 직접 할당하는 것이 빠를 것 같다.

count = 0
for t in temp:
    if 1 <= t[0] + i <= 8:
        if 1 <= t[1] + j <= 8:
            count += 1
