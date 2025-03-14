import sys

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

num, scale = list(map(int, sys.stdin.readline().split()))

b = []
while True:
    re = num % scale
    num = num // scale
    b.append(re)
    if num == 0:
        break
b.reverse()

for i in range(len(b)):
    if b[i] > 9:
        print(a[n.index(b[i])], end="")
    else:
        print(b[i], end="")