def solution(rows, columns, queries):
    answer = []
    matrix = [[i + j*columns for i in range(1, columns+1)] for j in range(0,rows)]
    for query in queries:
        r1,c1,r2,c2 = [i-1 for i in query]
        tt = []
        for i, row in enumerate(matrix):
            for j, ele in enumerate(row):
                if (r1<=i<=r2 and c1<=j<=c2) and (i==r1 or i ==r2 or j==c1 or j==c2): #테두리 요소들만 추출
                    if (i==r1 and j==c1) or (i==r1 and j!=c1 and j!=c2): # r1에서 오른쪽으로 움직이는 요소
                        tt.append((i,j+1,ele))
                    elif i==r1 and j==c2: #테두리 우상단 
                        tt.append((i+1,j,ele))
                    elif (i!=r1 and i!=r2): #테두리의 상단 하단이 아닌 요소들
                        if j==c1:
                            tt.append((i-1,j,ele))
                        elif j==c2:
                            tt.append((i+1,j,ele))
                    elif (i==r2 and j==c2) or (i==r2 and j!=c1 and j!=c2): #테두리 하단에서 좌하단이 아닌요소
                        tt.append((i, j-1,ele))
                    elif i==r2 and j==c1: #테두리 좌하단
                        tt.append((i-1, j, ele))

        answer.append(min(list(zip(*tt))[2]))

        for x,y,ele in tt:
            matrix[x][y] = ele
    
    return answer

'''
배열 요소를 순회하면서 조회한다.
조회 중 테두리 요소라면 각 조건에 맞추어 행,열 값을 바꿔준 (행, 열, 요소) 튜플을 수정할 배열을 모아놓은 요소에 추가한다.
조회가 끝나면
수정할 배열이 모여있는 요소를 순회하면서 알맞은 행,열 좌표에 새로운 값을 넣어준다.
'''