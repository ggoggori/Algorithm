n, m = 3,3
#array = "3 1 2\n4 1 4\n 2 2 2"
array = "7 3 1 8\n3 3 3 4"

array = [list(map(int,i.split())) for i in array.split('\n')]

temp = []
for i in array:
    temp.append(min(i))
print(max(temp))

'''
책에는 for 문에서 min_value를 계속 대입하고,
max로 min_value와 현재 최대값을 비교하여 최대값을 계속 갱신하는 방식을 사용!
max 안에는 iterator만 들어가는 줄 알았는데
max(1,2,3,4) 이런 식으로 그냥 사용도 가능하구나! 
'''