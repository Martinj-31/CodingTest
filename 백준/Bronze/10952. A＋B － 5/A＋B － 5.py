import sys

while True:
    x = list(map(int, sys.stdin.readline().split()))
    if x[0] == 0 and x[1] == 0:
        break
    print(x[0] + x[1])
    