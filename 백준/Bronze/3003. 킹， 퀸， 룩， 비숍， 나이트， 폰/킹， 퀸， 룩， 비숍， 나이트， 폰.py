import sys

ans = [1, 1, 2, 2, 2, 8]

X = list(map(int, sys.stdin.readline().split()))

for i in range(len(ans)):
    print(ans[i] - X[i], end=" ")