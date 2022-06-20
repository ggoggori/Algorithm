n = int(input())
array = [(input().split()) for _ in range(n)]
array = sorted(array, key=lambda x:int(x[1]))

for i in array:
    print(i[0], end=' ')