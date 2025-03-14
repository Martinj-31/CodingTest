import sys

N, M = map(int, sys.stdin.readline().split())
bin = [0] * N

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for t in range(i - 1, j):
        bin[t] = k

for i in range(N):
    print(bin[i], end=" ")
