import sys

N = int(sys.stdin.readline())

def dfs(x, y, num):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False

    if MAP[x][y] == 1:
        MAP[x][y] = num
        
        dfs(x - 1, y, num)
        dfs(x, y - 1, num)
        dfs(x + 1, y, num)
        dfs(x, y + 1, num)
        return True
    else: return False

MAP = []
for _ in range(N):
    MAP.append(list(map(int, input())))

num = 2
obstacle = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j, num) == True:
            obstacle += 1
            num += 1

cnt = 0
obstacle_ea = []
for i in range(2, num):
    for j in range(N):
        for k in range(N):
            if MAP[j][k] == i:
                cnt += 1
    obstacle_ea.append(cnt)
    cnt = 0
obstacle_ea = sorted(obstacle_ea)
print(obstacle)
for i in range(len(obstacle_ea)):
    print(obstacle_ea[i])