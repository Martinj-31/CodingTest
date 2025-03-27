import sys

A, B = map(int, sys.stdin.readline().split())

gA = list(map(int, sys.stdin.readline().split()))
gB = list(map(int, sys.stdin.readline().split()))

group = {}
for i in gA + gB:
    group[i] = []

for i in gA:
    group[i].append("A")
for i in gB:
    group[i].append("B")

cnt = 0
for i in group.values():
    if len(i) == 1:
        cnt += 1

print(cnt)
