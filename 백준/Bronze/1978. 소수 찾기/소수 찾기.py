import sys, math

N = int(sys.stdin.readline())

cnt = 0
n = list(map(int, sys.stdin.readline().split()))
for i in n:
    for x in range(2, i + 1):
        if i % x == 0:
            if i == x:
                cnt += 1
            break

print(cnt)
