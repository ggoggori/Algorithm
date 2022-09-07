from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque([])

for _ in range(n):
    string = sys.stdin.readline().split()
    if "push_front" == string[0]:
        queue.appendleft(int(string[1]))
        
    elif "push_back" == string[0]:
        queue.append(int(string[1]))

    elif string[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif string[0] == "pop_back":
        if queue:
            print(queue.pop())
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
