import sys

N, M = map(int, sys.stdin.readline().split())
group = [sys.stdin.readline() for _ in range(N)]

cnt = 0
for i in range(M):
    sentence = sys.stdin.readline()
    if sentence in group:
        cnt += 1

print(cnt)