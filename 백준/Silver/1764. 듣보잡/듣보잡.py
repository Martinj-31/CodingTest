import sys

N, M = map(int, sys.stdin.readline().split())

names = {}
for i in range(N):
    name = sys.stdin.readline().rstrip()
    names[name] = 1

cnt = 0
for i in range(M):
    name = sys.stdin.readline().rstrip()
    if name in names.keys():
        names[name] += 1
        cnt += 1
    else:
        names[name] = 1

names = dict(sorted(names.items()))
print(cnt)
for i in names.keys():
    if names[i] == 2:
        print(i)