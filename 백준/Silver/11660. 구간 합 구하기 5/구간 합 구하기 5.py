import sys

N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def prefix_sum(n):
    g = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            g[i][j] = g[i - 1][j] + g[i][j - 1] - g[i - 1][j - 1] + graph[i - 1][j - 1]
    return g


p_sum = prefix_sum(N)
for m in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(p_sum[x2][y2] - p_sum[x1 - 1][y2] - p_sum[x2][y1 - 1] + p_sum[x1 - 1][y1 - 1])