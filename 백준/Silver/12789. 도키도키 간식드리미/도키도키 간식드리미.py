import sys
from collections import deque

N = int(sys.stdin.readline())
order = deque((map(int, sys.stdin.readline().split())))
temp = []

cnt = 1
t = 0
canOut = False
while True:
    if len(temp) == 0:
        first = order.popleft()
        if first != cnt:
            temp.append(first)
        else:
            cnt += 1
    elif len(order) == 0:
        first = temp.pop()
        if first != cnt:
            order.append(first)
        else:
            cnt += 1
    elif order[0] < temp[-1]:
        first = order.popleft()
        if first != cnt:
            temp.append(first)
        else:
            cnt += 1
    elif order[0] > temp[-1]:
        first = temp.pop()
        if first != cnt:
            temp.append(first)
        else:
            cnt += 1
    t += 1

    if len(order) == 0 and len(temp) == 0:
        canOut = True
        break
    elif t > 2*N:
        break

if canOut:
    print("Nice")
else:
    print("Sad")