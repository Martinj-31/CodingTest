import sys

N = int(sys.stdin.readline())
mem = list(map(int, sys.stdin.readline().split()))
mem.sort()
cnt = 0
total = 0
for i in mem:
    cnt = i + cnt
    total += cnt
print(total)
