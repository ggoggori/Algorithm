n = int(input())
temp = [0,0,0]
count = 0

while temp[0] != n+1:
    temp[2] += 1
    if temp[2] == 60:
        temp[2] = 0
        temp[1] += 1
    if temp[1] == 60:
        temp[1] = 0
        temp[0] += 1
    if True in [True for i in list(map(str,temp)) if '3' in i]:
        count += 1
    