import sys

n = int(sys.stdin.readline())

Fs = list(map(int, sys.stdin.readline().split()))

max = -100
for i in range(len(Fs)-1):
    for j in range(1, len(Fs)-i):
        a = Fs[i]*Fs[j+i]
        if a > max:
            max = a
        else: pass
print(max)
