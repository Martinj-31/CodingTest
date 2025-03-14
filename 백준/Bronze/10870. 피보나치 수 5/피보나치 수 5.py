import sys

N = int(sys.stdin.readline())

a0, a1 = 0, 1

for i in range(N - 1):
    a2 = a0 + a1
    a0, a1 = a1, a2

if N == 0:
    print(a0)
elif N == 1:
    print(a1)
else: print(a2)