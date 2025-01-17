import sys

A, B = map(int, sys.stdin.readline().split())

if A > B:
    print(f"A")
elif A < B:
    print(f"B")
else: print(f"same")
