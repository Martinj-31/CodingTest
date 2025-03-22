import sys

T = int(sys.stdin.readline())
houses = [[0 for _ in range(15)] for _ in range(15)]

for i in range(15):
    for j in range(15):
        if i == 0:
            houses[i][j] = j
            continue
        houses[i][j] = sum(houses[i - 1][:j + 1])

for t in range(T):
    print(houses[int(sys.stdin.readline())][int(sys.stdin.readline())])