import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())

r = 0
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    r += a * b

if r == X:
    print("Yes")
else:
    print("No")