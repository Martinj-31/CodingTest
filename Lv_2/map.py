import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    dots = (2**i+1)**2
print(dots)