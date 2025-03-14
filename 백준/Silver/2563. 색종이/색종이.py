import sys

N = int(sys.stdin.readline())

board = [[0] * 100 for _ in range(100)]

r = 0
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())

    for j in range(a, a + 10):
        for k in range(b, b + 10):
            if board[j][k] == 0:
                board[j][k] = 1
                r += 1

print(r)