input = "5 8 3 \n2 4 5 4 6"
answer = 46

n, m, k = list(map(int, input.split("\n")[0].split()))
array = sorted(list(map(int, input.split("\n")[1].split())), reverse=True)

idx, restrict, sum = 0, 0, 0
for _ in range(m):
    if restrict == k:
        sum += array[idx + 1]
        restrict = 0
        continue
    else:
        sum += array[idx]
    restrict += 1

# 사실 idx는 0과 1만 사용하면 되는데, 잘못했다!

