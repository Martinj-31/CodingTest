import sys

N = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))

max_num = 1
for i in range(2, max(n) + 1):
    cnt = 0
    for j in range(N):
        if n[j] % i == 0:
            cnt += 1
    if cnt > max_num:
        max_num = cnt

print(max_num)