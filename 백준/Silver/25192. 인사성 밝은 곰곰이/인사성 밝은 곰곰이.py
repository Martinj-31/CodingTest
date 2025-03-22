import sys
from collections import Counter

N = int(sys.stdin.readline())

names = []
cnt = 0
for i in range(N):
    com = sys.stdin.readline().rstrip()
    if com == "ENTER":
        names = Counter(names)
        cnt += len(names)
        names = []
    elif i == N - 1 and com != "ENTER":
        names.append(com)
        names = Counter(names)
        cnt += len(names)
        names = []
    elif i == N - 1 and com == "ENTER":
        names = Counter(names)
        cnt += len(names)
        names = []
    else:
        names.append(com)

print(cnt)