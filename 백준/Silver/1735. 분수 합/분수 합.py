import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())


def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y

N = gcd(a*d + b*c, b*d)

print((a*d + b*c) // N, b*d // N)