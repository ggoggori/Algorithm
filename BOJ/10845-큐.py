from collections import deque
import sys

# readline 쓰면 뒤에 개행문자가 붙는 걸 몰라서 엄청 오래걸렸다 ㅠ

n = int(sys.stdin.readline())
queue = deque([])

for _ in range(n):
    string = sys.stdin.readline().split()
    if "push" in string[0]:
        queue.append(int(string[1]))

    elif string[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif string[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif string[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

    elif string[0] == "size":
        print(len(queue))

    elif string[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
