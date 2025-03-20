import sys

N = int(sys.stdin.readline())


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


print(factorial(N))