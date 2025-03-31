import sys

T = int(sys.stdin.readline())

for t in range(T):
    N = int(sys.stdin.readline())
    a, b = 1, 0
    for i in range(N):
        a, b = b, a + b
    print(a, b)
