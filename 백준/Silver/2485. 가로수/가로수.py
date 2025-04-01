import sys

N = int(sys.stdin.readline())

trees = [int(sys.stdin.readline()) for _ in range(N)]


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


gap = []
for i in range(1, N):
    gap.append(trees[i] - trees[i - 1])

g = gap[0]
for i in range(1, len(gap)):
    g = gcd(g, gap[i])

cnt = 0
for i in gap:
    cnt += i // g - 1

print(cnt)