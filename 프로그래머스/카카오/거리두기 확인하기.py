a, b = [1,0,0,-1], [0,1,-1,0]

def check_p(place): 
    '''
    P를 발견하면 P의 위치에서 상하좌우를 살핀다.
    상하좌우를 살폈을 때 O(빈테이블)이 발견되면 Check_o를 실행한다.(거리가 2까지 가능하기 때문에 P와 P사이에 O가 있을 가능성을 체크해보는 것.)
    '''
    n, m = len(place), len(place[0])
    for i in range(0, n):
        for j in range(0, m):
            if place[i][j] == 'P':
                for k in range(4):
                    if (0<=i+a[k]<n and 0<=j+b[k]<m) and (place[i+a[k]][j+b[k]]=='O' or place[i+a[k]][j+b[k]]=='P'):
                        if place[i+a[k]][j+b[k]]=='O':
                            if check_O(place,i,j,i+a[k],j+b[k]):
                                return True
                        else:
                            return True
    
    return False
            
def check_O(place,i,j,x,y):
    """
    현재 위치를 기점으로 상하좌우를 살펴서 P가 나오면 True(거리두기를 지키지 못하고 있음)를 반환한다.
    이 때 전 기점 P는 제외해야 한다.
    """
    n, m = len(place), len(place[0])
    for k in range(4):
        if (0<=x+a[k]<n and 0<=y+b[k]<m) and (place[x+a[k]][y+b[k]]=='P') and (i!=x+a[k] and j!=y+b[k]):
            return True
    return False
    
def solution(places):
    answer = []
    for place in places:
        answer.append(0 if check_p(place) else 1)
        
    return answer

'''
문제를 보고 어렵다고 생각하면, 기부터 죽는 것 같다...
어렵더라도 문제를 보고 문제 자체에 숨어있는 규칙을 찾자
문제 표면에 있는 것을 구현하려고 하면 막막할 뿐!
'''