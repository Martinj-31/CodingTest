import sys

a = [[-1] * 15 for _ in range(5)]

b = []
for i in range(5):
    b.append(list(sys.stdin.readline().rstrip()))

for i in range(5):
    for j in range(len(b[i])):
        a[i][j] = b[i][j]

for i in range(15):
    for j in range(5):
        if a[j][i] != -1:
            print(a[j][i], end="")