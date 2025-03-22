import sys

A, B = map(int, sys.stdin.readline().split())


def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b


def lcm(a, b):
    return a * b // gcd(A, B)


print(gcd(A, B))
print(lcm(A, B))