import sys

N, M = map(int, sys.stdin.readline().split())

pockemon = {}
for i in range(N):
    name = sys.stdin.readline().rstrip()
    pockemon[name] = str(i + 1)
    pockemon[str(i + 1)] = name

for i in range(M):
    info = sys.stdin.readline().rstrip()
    print(pockemon[info])
