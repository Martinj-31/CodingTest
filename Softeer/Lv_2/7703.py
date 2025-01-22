import sys

N = int(sys.stdin.readline())

result = []
for _ in range(N):
    S, T = sys.stdin.readline().split()
    for i in range(len(S)):
        if S[i] == 'x' or S[i] == 'X':
            r = T[i]
            print(r.upper(), end='')