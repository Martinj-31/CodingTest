import sys, math
from collections import deque

T = int(sys.stdin.readline())

for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    values = list(map(int, sys.stdin.readline().split()))

    q = deque([i for i in range(N)])
    vq = deque(values)

    cnt = 0
    while True:
        for i in range(1, len(vq)):
            if vq[0] < vq[i]:
                q.append(q.popleft())
                vq.append(vq.popleft())
                break
        else:
            printer = q.popleft()
            vq.popleft()
            cnt += 1
            if printer == M:
                break
    print(cnt)