from collections import deque

def solution(maps):
    answer = -1
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))
    
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                print(visited[nx][ny])
                q.append((nx, ny))
            if nx == n - 1 and ny == m - 1:
                answer = visited[nx][ny]

    return answer