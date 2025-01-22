import sys

W, N = map(int, sys.stdin.readline().split())

j = []
for _ in range(N):
    j.append(list(map(int, sys.stdin.readline().split())))
j = sorted(j, key=lambda x:x[1], reverse=True)

price = 0
for i in range(N):
    if j[i][0] < W:
        price += j[i][0] * j[i][1]
        W -= j[i][0]
    elif j[i][0] >= W:
        price += W * j[i][1]
        W = 0
    else: pass
print(price)