import sys

N = int(sys.stdin.readline())
Ns = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
Ms = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if Ms[i] in Ns:
        print(1)
    else:
        print(0)