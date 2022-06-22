def pibo(x):
    d = [0] * (x+1)
    d[1] = 1 #0은 그냥 계산할 때 안쓰니까 버림!!
    d[2] = 1

    for i in range(3, x+1):
        d[i] = d[i-1] + d[i-2]

    return d[x]