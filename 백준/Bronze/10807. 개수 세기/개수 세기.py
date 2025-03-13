import sys

N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
result = 0
for i in range(N):
    if a[i] == b:
        result += 1

print(result)