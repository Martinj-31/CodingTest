import sys

N, M = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

mini = 50 * 50
for i in range(N - 7):
    for j in range(M - 7):
        now = "B"
        cnt = 0
        for x in range(8):
            start = now
            for y in range(8):
                if board[i+x][j+y] != now:
                    cnt += 1
                if now == "B":
                    now = "W"
                else:
                    now = "B"
            if start == "B":
                now = "W"
            else:
                now = "B"
        if cnt < mini:
            mini = cnt

        now = "W"
        cnt = 0
        for x in range(8):
            start = now
            for y in range(8):
                if board[i+x][j+y] != now:
                    cnt += 1
                if now == "W":
                    now = "B"
                else:
                    now = "W"
            if start == "W":
                now = "B"
            else:
                now = "W"
        if cnt < mini:
            mini = cnt

print(mini)