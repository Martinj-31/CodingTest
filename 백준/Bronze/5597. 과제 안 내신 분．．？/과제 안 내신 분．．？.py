import sys

a = []
for i in range(28):
    a.append(int(sys.stdin.readline()))
a.sort()
for i in range(1, 31):
    if i not in a:
        print(i)