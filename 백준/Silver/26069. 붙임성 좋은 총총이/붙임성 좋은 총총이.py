import sys
from collections import Counter

N = int(sys.stdin.readline())

dance = set()

for i in range(N):
    a, b = sys.stdin.readline().split()

    if a == "ChongChong" or b == "ChongChong":
        dance.add(a)
        dance.add(b)

    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)

print(len(dance))