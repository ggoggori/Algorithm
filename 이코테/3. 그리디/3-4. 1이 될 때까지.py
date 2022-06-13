n, k = 25, 5
count = 0

while True:
    count += 1
    if n % k == 0:
        n //= k
    else:
        n -= 1

    if n == 1:
        break