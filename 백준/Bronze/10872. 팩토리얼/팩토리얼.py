import sys

N = int(sys.stdin.readline())

r = 1
for i in range(1, N+1):
    r *= i
print(r)