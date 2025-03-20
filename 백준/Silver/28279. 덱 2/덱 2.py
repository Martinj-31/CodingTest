import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque()
for _ in range(N):
    com = list(map(int, sys.stdin.readline().split()))

    if com[0] == 1:
        q.appendleft(com[1])
    elif com[0] == 2:
        q.append(com[1])
    elif com[0] == 3:
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif com[0] == 4:
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)
    elif com[0] == 5:
        print(len(q))
    elif com[0] == 6:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 7:
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif com[0] == 8:
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)