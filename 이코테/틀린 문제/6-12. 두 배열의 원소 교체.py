n, k = 5, 3
a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

for _ in range(k):
    min_index = a.index(min(a))
    max_index = b.index(max(b))
    a[min_index], b[max_index] = b[max_index], a[min_index]
    # 현재 로직에는 a의 min 값보다 b의 max 값이 작아도 교환이 된다.
