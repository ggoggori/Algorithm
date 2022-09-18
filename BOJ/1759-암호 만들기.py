from itertools import combinations
l, c = map(int, input().split())

temp = [i for i in input().split()]

check_list = ['a','e','i','o','u'] # 모음 리스트
answer = []
for i in map(list, list(combinations(temp, l))): #가능한 모든 조합들을 전수 조사(브루트 포스)
    box = []

    for char in check_list: # 모음 하나씩 꺼내서 확인
        if char in i: #만약 모음이 있다면
            i.remove(char) #지우고
            box.append(char) #임시 리스트에 넣음
    
    if len(box) >= 1 and len(i) >= 2: # 임시리스트에 있는 모음이 1개 이상이고, 모음이 없는 리스트. 그러니까 자음만 있는 리스트가 2보다 크다면
        i.extend(box) # 두 리스트를 합침
        i.sort() # 정렬
        answer.append(''.join(i)) # 문자열로 변환

for i in sorted(answer):
    print(i)