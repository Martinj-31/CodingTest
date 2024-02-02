import sys

N = int(sys.stdin.readline())

x_south, y_south = map(int, sys.stdin.readline().split())
for i in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    if y < y_south:
        x_south = x
        y_south = y
print(x_south, y_south) 
