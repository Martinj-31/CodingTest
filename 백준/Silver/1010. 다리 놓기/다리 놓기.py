import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    n, m = 1, 1
    for i in range(N):
        n *= (N - i)
        m *= (M - i)
    print(m // n)