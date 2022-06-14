n = list(input())
if len(n) == 1:
    n.append('0')

target = n
count = 0
while True:
    count += 1
    n = list(map(int, n))
    new = n[0] + n[1]
    n = list(str(n[1]) + list(str(new))[-1])
    if n == target:
        break

print(count)