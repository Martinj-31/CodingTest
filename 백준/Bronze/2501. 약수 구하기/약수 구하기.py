import sys, math

N, K = map(int, sys.stdin.readline().split())

cnt = 0
result = -1
for i in range(1, N + 1):
    if N % i == 0:
       cnt += 1
       if cnt == K:
           result = i
           break

if result == -1:
    print(0)
else:
    print(result)