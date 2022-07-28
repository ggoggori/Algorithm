# 틀림!!
# 넘 어렵다..
def solution(n, build_frame):
    answer = []
    condition = [[5] * (n + 1) for _ in range(n + 1)]

    for frame in build_frame:
        x, y, a, b = frame

        if a == 0 and b == 1:  # 기둥 설치
            if y == 0:  # 바닥이라면
                condition[x][y] = 1
                answer.append([x, y, a])
            elif y != 0:  # 바닥이아니라면
                if condition[x][y - 1] == 1 or condition[x - 1][y] == 0:
                    # 적어도 아래가 기둥이거나 또는 왼쪽이 보 여야함.
                    condition[x][y] = 1
                    answer.append([x, y, a])
                else:  # 바닥, 기둥, 보 모두 아니라면 패스
                    continue

        elif a == 0 and b == 0:  # 기둥 삭제
            if condition[x][y + 1] == 1:  # 만약 삭제하려는 기둥 위가 보 라면
                if condition[x - 1][y + 1] == 1:
                    answer = [i for i in answer if not (i[0] == x and i[1] == y)]  # 조건 필터링
            elif condition[x][y - 1] == 1:  # 만약 삭제하려는 기둥 아래가 보 라면
                if condition[x - 1][y] == 1:
                    answer = [i for i in answer if not (i[0] == x and i[1] == y)]  # 조건 필터링

        elif a == 1 and b == 1:  # 보 설치
            if condition[x][y - 1] == 1 or condition[x + 1][y - 1] == 1:  # 아래 or 오른쪽 아래가 기둥이라면 설치
                condition[x][y] = 0
                answer.append([x, y, a])

            elif condition[x - 1][y] == 0 and condition[x + 1][y] == 0:
                # 양쪽이 모두 보라면 설치
                condition[x][y] = 0
                answer.append([x, y, a])

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))

