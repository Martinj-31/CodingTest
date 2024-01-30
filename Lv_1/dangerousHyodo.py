import sys

a, b, d = map(int, sys.stdin.readline().split())

time = 1
step = 0
front = a
back = b
for distance in range(1, d*2):
    step += 1
    if step == front:
        if step == d:
            front = b
            back = a
        else: time += back
        step = 0
    elif distance == d:
        step = 0
        front = b
        back = a
    else: pass
    time += 1
print(time)