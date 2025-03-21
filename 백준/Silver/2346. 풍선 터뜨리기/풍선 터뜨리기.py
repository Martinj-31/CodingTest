import sys
from collections import deque

N = int(sys.stdin.readline())
bal = deque(list(map(int, sys.stdin.readline().split())))
order = deque([i for i in range(1, N + 1)])

result = []
result.append(order[0])
for _ in range(N - 1):
    dir = bal[0]
    bal[0] = 0

    if dir > 0:
        cnt = 0
        while cnt != dir:
            a = bal.popleft()
            bal.append(a)

            b = order.popleft()
            order.append(b)

            if bal[0] != 0:
                cnt += 1
    elif dir < 0:
        cnt = 0
        while cnt != dir:
            a = bal.pop()
            bal.appendleft(a)

            b = order.pop()
            order.appendleft(b)

            if bal[0] != 0:
                cnt -= 1

    result.append(order[0])

for i in result:
    print(i, end=" ")