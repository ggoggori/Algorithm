x = 99
d = [0] * (x + 1)


def pibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]

    d[x] = pibo(x - 1) + pibo(x - 2)
    return d[x]
