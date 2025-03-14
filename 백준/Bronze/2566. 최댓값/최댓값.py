import sys

a = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

mi = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if a[i][j] > mi:
            mi = a[i][j]
            x, y = i, j

print(mi)
print(x + 1, y + 1)