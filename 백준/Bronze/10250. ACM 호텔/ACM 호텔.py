import sys

T = int(sys.stdin.readline())

for t in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    floor = N % H
    num = N // H + 1
    if floor == 0:
        floor = H
        num -= 1

    print(floor*100 + num)