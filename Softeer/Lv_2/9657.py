import sys

n, m = map(int, sys.stdin.readline().split())

forest = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(2):
    beam = [0 for _ in range(n)]
    start, end = map(int, sys.stdin.readline().split())
    
    for idx in range(start, end + 1):
        beam[idx - 1] = 1

    for j in range(m):
        for k in range(n):
            if forest[k][j] == 1 and beam[k] == 1:
                forest[k][j], beam[k] = 0, 0

cnt = 0
for i in range(n):
    for j in range(m):
        if forest[i][j] == 1:
            cnt += 1

print(cnt)