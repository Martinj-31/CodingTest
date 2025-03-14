import sys

N = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

m = max(a)

for i in range(N):
    a[i] = a[i] / m * 100

print(sum(a) / len(a))