# 푼 횟수 : 
# 후기: 코드가 지저분하고 test case를 맞추기 위해서 거기에 코드를 끼워 맞춘다는 느낌이 강하게 들었다.
# 다음에는 효율적이고 보기 쉬운 코드로 작성해보려고 노력하자!
# 맞은 줄 알았는데, 백준에 제출해보니 틀렸다!

# input
n = int(input())
k = int(input())

apples = []
for _ in range(k):
    x, y = list(map(int, input().split()))
    apples.append((x, y))

l = int(input())
XC = []
for _ in range(l):
    x, c = input().split()
    XC.append((int(x), c))

################################################################################################################
from collections import deque

array = [[0] * n for _ in range(n)]

for apple in apples:
    x, y = apple
    array[x - 1][y - 1] = 1

count = 1
dx = deque([0, 1, 0, -1])  # 우하좌상
dy = deque([1, 0, -1, 0])
direction = (dx[0], dy[0])
cur_x, cur_y = 0, 0
array[cur_x][cur_y] = "s"
length = 0
tracks = []  # 꼬리의 위치를 저장하기 위한 리스트, 만약 다음에 움직일 좌표가 tracks 리스트 안에 있다면 game over!

while True:
    count += 1
    tracks.append((cur_x, cur_y))
    array[cur_x][cur_y] = 0  # 지나간 길은 다시 0으로 바꿔줌.

    cur_x, cur_y = cur_x + dx[0], cur_y + dy[0]

    if cur_x < 0 or cur_y < 0 or cur_x > n - 1 or cur_y > n - 1:  # 격자를 벗어난다면 game over!
        break

    if array[cur_x][cur_y] == 1:  # 사과라면 꼬리를 늘린다.
        length += 1
        array[cur_x][cur_y] = "s"

    elif array[cur_x][cur_y] == 0:
        array[cur_x][cur_y] = "s"

    tracks = tracks[-(length + 1) :]
    # (length에 1을 더해준 이유는 뱀이 움직이는 순간에는 추적해야할 꼬리가 순간적으로 늘어나기 때문!) ,, 하지만 비효율적인 것 같다.

    if (cur_x, cur_y) in tracks:
        break

    if count in [i[0] for i in XC]:  # 방향 바꾸기
        for xc_ in XC:
            x = xc_[0]
            c = xc_[1]
            if count == x:
                break
        if c == "D":  # 오른쪽 회전
            dx.rotate(-1)
            dy.rotate(-1)
        else:  # 왼쪽 회전
            dx.rotate(1)
            dy.rotate(1)

print(count)
