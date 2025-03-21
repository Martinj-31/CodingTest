import sys

N, K = map(int, sys.stdin.readline().split())

n, k = 1, 1
for i in range(K):
    n *= (N - i)
    k *= (K - i)

print(n // k)