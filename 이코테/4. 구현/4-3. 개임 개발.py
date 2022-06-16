n,m = map(int, input().split())
n_, m_, direction = map(int, input().split())
array = []
for  i in range(n):
    array.append(list(map(int, input().split())))

dx = [0,-1,0,1] #북 서 남 동
dy = [-1,0,1,0]

count = 0
kan = 1

while True:
    direction += 1
    if direction == 4:
        direction = 0

    x ,y = dx[direction], dy[direction]
    next_n, next_m = n_+x, m_+y
    if next_n == n or next_m == m:
        continue
    if array[next_n][next_m] == 1:
        count += 1
        if count == 4:
            if direction >=3: # prevent dicrection from out of range 
                direction -= 2
            else:
                direction += 2
            x ,y = dx[direction], dy[direction]
            n_, m_ = n_+x, m_+y
            if n_ == n or m_ == m: #뒤돌아서 가야하는 칸이 n,m 바깥일 때 break(사실 문제에서는 맵의 바깥 쪽은 모두 바다라고 설정하기 때문에 이게 들어갈 일은 없음.)
                break
            if array[n_][m_] == 1: #뒤돌아서 가야하는 칸이 바다이거나, 이미 갔다온 칸이면 break
                break
        
    else:
        array[n_][m_] = 1
        n_, m_ = next_n, next_m
        kan += 1
        count = 0       