import sys

gnd = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

min_cost = 100000
for i in range(3):
    for j in range(3):
        cost = abs(gnd[i][int((j+1) % 3)] - gnd[i][int(j % 3)]) + abs(gnd[i][int((j+2) % 3)] - gnd[i][int(j % 3)])
        if cost < min_cost:
            min_cost = cost

for i in range(3):
    for j in range(3):
        cost = abs(gnd[int((i+1) % 3)][j] - gnd[int(i % 3)][j]) + abs(gnd[int((i+2) % 3)][j] - gnd[int(i % 3)][j])
        if cost < min_cost:
            min_cost = cost
print(min_cost)