import sys

cnt = int(sys.stdin.readline())

cand = list(map(int, sys.stdin.readline().split()))
cand.sort()

print(cand[0]*cand[-1])