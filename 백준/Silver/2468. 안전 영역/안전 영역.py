from collections import deque

N = int(input())

region = [list(map(int, input().split())) for _ in range(N)]


def check(graph):
    for i in range(N):
        print(graph[i])


def bfs(x, y):
    global count
    queue = deque([])
    queue.append((x, y))
    check_region[x][y] = 0
    count += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if check_region[nx][ny] == 1:
                check_region[nx][ny] = 0
                queue.append((nx, ny))


max_rain = max(map(max, region))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count_list = []
max_region = 0
for rain in range(max_rain):
    count = 0
    check_region = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if region[i][j] > rain:
                check_region[i][j] = 1
    for i in range(N):
        for j in range(N):
            if check_region[i][j] == 1:
                bfs(i, j)

    count_list.append(count)

print(max(count_list))
