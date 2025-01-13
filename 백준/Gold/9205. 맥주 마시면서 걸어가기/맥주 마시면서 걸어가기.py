import sys
from collections import deque


def bfs():
    q = deque()
    q.append((home[0], home[1]))
    while q:
        x, y = q.popleft()
        if abs(x - dest[0]) + abs(y - dest[1]) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                if abs(x - conv[i][0]) + abs(y - conv[i][1]) <= 1000:
                    visited[i] = 1
                    q.append((conv[i][0], conv[i][1]))
    print('sad')
    return


T = int(sys.stdin.readline())

for t in range(T):
    n = int(sys.stdin.readline())
    home = list(map(int, sys.stdin.readline().split()))
    conv = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dest = list(map(int, sys.stdin.readline().split()))
    visited = [0 for _ in range(n + 1)]

    bfs()

