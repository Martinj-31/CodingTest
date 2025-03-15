import sys, math

A, B, V = map(int, sys.stdin.readline().split())

x = (V - B) / (A - B)
print(int(x) if x == int(x) else int(x) + 1)
