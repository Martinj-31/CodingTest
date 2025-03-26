import sys

N = int(sys.stdin.readline())

cnt = [0] * 2000001

for _ in range(N):
    num = int(sys.stdin.readline())
    cnt[num] += 1

for i in range(-1000000, 1000001):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)