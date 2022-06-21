n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    try:
        array.index(i)
    except:
        print('no', end=' ')
        continue
    print('yes', end=' ')