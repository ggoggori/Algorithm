from itertools import combinations

candidate = []
for _ in range(9):
    temp = int(input())
    candidate.append(temp)

for i in list(combinations(candidate, 7)):
    if sum(i) == 100:
        for t in sorted(i):
            print(t)
        break
