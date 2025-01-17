import sys

iter = int(sys.stdin.readline())

test = [list(map(int, sys.stdin.readline().split())) for i in range(iter)]

for i in range(iter):
  print(f"Case #{i+1}: {test[i][0]+test[i][1]}")
  