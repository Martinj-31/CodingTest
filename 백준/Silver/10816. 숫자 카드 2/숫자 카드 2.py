import sys
from collections import Counter

N = int(sys.stdin.readline())
Ns = Counter(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
Ms = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    print(Ns[Ms[i]], end=" ")