import sys

n = int(sys.stdin.readline())

village = list(map(int, sys.stdin.readline().split()))

cnt = 1
short = village[1] - village[0]
for i in range(1, len(village)-1):
    if village[i+1] - village[i] < short:
        short = village[i+1] - village[i]
        cnt = 1
    elif village[i+1] - village[i] == short:
        cnt += 1
    else: pass
print(cnt)
