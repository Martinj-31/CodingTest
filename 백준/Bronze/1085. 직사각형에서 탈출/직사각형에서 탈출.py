import sys

x, y, w, h = map(int, sys.stdin.readline().split())

print(min(min(y, h - y), min(x, w - x)))