array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

idx_array = [0] * (max(array)+1) # array의 최대값 만큼의 크기를 가지는 리스트 생성

for i in array:
    idx_array[i] += 1 # 갯수를 셈

for i in range(len(idx_array)): # 갯수를 기반으로 정렬된 리스트를 생성
    for _ in range(idx_array[i]):
        print(i, end=' ')