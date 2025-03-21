import sys
from collections import deque

N = int(sys.stdin.readline())
queueORstack = list(map(int, sys.stdin.readline().split()))
queuestack = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
C = list(map(int, sys.stdin.readline().split()))

q = deque()
for i in range(N):
    if queueORstack[i] == 0:
        q.appendleft(queuestack[i])

for i in range(M):
    q.append(C[i])
    print(q.popleft(), end=" ")
