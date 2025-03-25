import sys

N = int(sys.stdin.readline())
mem = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def team(L, idx):
    global minimum
    if L == N // 2:
        start = 0
        link = 0
        for ii in range(N):
            for iii in range(N):
                if visited[ii] == 1 and visited[iii] == 1:
                    start += mem[ii][iii]
                elif visited[ii] == 0 and visited[iii] == 0:
                    link += mem[ii][iii]
        minimum = min(minimum, abs(start - link))
        return

    for i in range(idx, N):
        if visited[i] == 0:
            visited[i] = 1
            team(L + 1, i + 1)
            visited[i] = 0


minimum = 1e9
visited = [0 for i in range(N)]
team(0, 0)
print(minimum)
